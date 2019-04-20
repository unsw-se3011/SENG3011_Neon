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
    waiting: false,
    start_date: toDate(year_before),
    end_date: toDate(date_now),
    location: "",
    key_term: "",
    count: 0,
    reports: [],
    // this for the make up id from ramen
    ramen_id: 0
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
    set_by_outbreak: (state, outbreak) => {
      state.start_date = outbreak.start_date;
      state.end_date = outbreak.end_date;
      state.key_term = outbreak.key_term;
    },
    // to support multiple api, we need introduce
    // async mechanism here
    commit_waiting: state => {
      // reset the ramen id
      state.ramen_id = 0;
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
    },
    inc_ramen_id: state => (state.ramen_id += 1),
    add_ramen_reports: (state, data) => {
      let reports = [];
      data.forEach(el => {
        let article = {
          url: el.url,
          date_of_publication: el.date_of_publication,
          headline: el.headline,
          main_text: el.main_text
        };
        // attach each artile into report
        // and makeup a temporary id
        el.reports.forEach(re => {
          re.id = "r" + state.ramen_id++;
          re.article = article;
          reports.push(re);
        });
      });
      // push the constructed report to database
      state.reports = [...state.reports, ...reports];
      state.waiting = false;
    },
    set_count: (state, count) => (state.count = count)
  },
  actions: {
    fetch_neon_reports: async ({ commit, dispatch }, next) => {
      /**
       * self recursing to fetch the data as a background activity
       */
      // remove the base url to get ride of cor
      next = next.replace("http://localhost:8000", "");

      let ret = await axios.get(next);
      commit("add_neon_reports", ret.data.results);

      // recursive self
      if (ret.data.next) {
        dispatch("fetch_neon_reports", ret.data.next);
      }
    },
    fetch_ramen_data: async ({ state, commit }) => {
      /**
       * Fetch from seng ramen
       */

      let start_date = new Date(Date.parse(state.start_date)).toISOString();
      let end_date = new Date(Date.parse(state.end_date)).toISOString();

      let ret = await axios.get(
        "https://sneg-ramen.herokuapp.com/api/articles",
        {
          params: {
            start_date: start_date.substring(0, 19),
            end_date: end_date.substring(0, 19),
            location: state.location,
            key_term: state.key_term
          }
        }
      );
      commit("add_ramen_reports", ret.data);
    },

    refresh_data: async ({ state, commit }, force = false) => {
      if (force == true) {
        commit("commit_waiting");
      } else if (
        (force == false && state.reports.length != 0) ||
        this.waiting == true
      ) {
        // we don't force list to update
        return;
      }
      // should fetch two database
      // from date format to iso format
      let start_date = new Date(Date.parse(state.start_date)).toISOString();
      let end_date = new Date(Date.parse(state.end_date)).toISOString();

      // start the transaction of db update
      /**
       * Fetch from neon project
       */
      let ret = await axios.get("/v0/reports/", {
        params: {
          start_date: start_date,
          end_date: end_date,
          location: state.location,
          key_term: state.key_term
        }
      });

      // this action probably will overflow the device
      // if (ret.data.next) {
      //   dispatch("fetch_neon_reports", ret.data.next);
      // }
      commit("set_count", ret.data.count);

      commit("add_neon_reports", ret.data.results);

      // dispatch("fetch_ramen_data");
      return ret;
    }
  }
};
