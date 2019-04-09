import axios from "axios";

/**
 * This is for attach the standard seng apis and provide the search
 * functionality with it
 */

function toDate(date) {
  return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;
}

function initial() {
  // calculate the default value for start date and end date
  let date_now = new Date();
  let year_before = new Date();
  year_before.setFullYear(date_now.getFullYear() - 1);
  return {
    filter_show: false,
    search_key: "",
    waiting: true,
    start_date: toDate(year_before),
    end_date: toDate(date_now),
    location: "",
    key_term: "",
    reports: []
  };
}

export default {
  namespaced: true,

  state: initial(),
  mutations: {
    toggle_filter: state => {
      // toggle the show boolean
      state.filter_show = !state.filter_show;
    },
    waiting: (sate, value) => (sate.waiting = value),
    set_start_date: (state, value) => (state.start_date = value),
    set_end_date: (state, value) => (state.end_date = value),
    set_location: (state, value) => (state.location = value),
    set_key_term: (state, value) => (state.key_term = value),
    // to support multiple api, we need introduce
    // async mechanism here
    commit_waiting: state => {
      state.waiting = true;
      state.reports = [];
    },
    add_reports: (state, value) => {
      state.reports = [...state.reports, ...value];
      state.waiting = false;
      // release the lock
    },
    add_neon_reports: (state, value) => {
      value = value.map(el => {
        el.id = "n" + el.id;
        return el;
      });
      state.reports = [...state.reports, ...value];
      state.waiting = false;
    }
  },
  actions: {
    fetch_reports: async ({ commit, dispatch }, next) => {
      /**
       * self recursing to fetch the data as a background activity
       */
      // remove the base url to get ride of cor
      next = next.replace("http://localhost:8000/v0", "");

      let ret = await axios.get(next);
      commit("add_neon_reports", ret.data.results);
      // recursive self
      if (ret.data.next) {
        console.log(ret.data.next);
        dispatch("fetch_reports", ret.data.next);
      }
    },
    refresh_data: async ({ state, commit, dispatch }) => {
      // should fetch two database
      // console.log("try to fetch the data");
      // console.log(new Date(Date.parse(state.start_date)).toISOString());
      // console.log(new Date(Date.parse(state.end_date)).toISOString());
      // start the transaction of db update
      commit("commit_waiting");
      let ret = await axios.get("/reports/", {
        params: {
          start_date: new Date(Date.parse(state.start_date)).toISOString(),
          end_date: new Date(Date.parse(state.end_date)).toISOString(),
          location: state.location,
          key_term: state.key_term
        }
      });

      // this action probably will overflow the device
      // if (ret.data.next) {
      //   dispatch("fetch_reports", ret.data.next);
      // }
      commit("add_neon_reports", ret.data.results);
      return ret;
    }
  }
};
