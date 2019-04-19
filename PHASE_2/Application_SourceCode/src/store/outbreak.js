import axios from "axios";

function initial() {
  return {
    waiting: true,
    outbreaks: [
      {
        id: 1,
        key_term: "zika",
        start_date: "2013-10-30",
        end_date: "2016-10-30"
      },
      {
        id: 2,
        key_term: "Ebola",
        start_date: "2013-12-14",
        end_date: "2016-01-14"
      }
    ]
  };
}

export default {
  namespaced: true,
  state: initial(),
  mutations: {
    commit_waiting: state => {
      // reset the ramen id
      state.waiting = true;
      state.outbreaks = [];
    },
    add_outbreaks: (state, value) => {
      // add the data array and pagination informations
      state.outbreaks = [...state.outbreaks, ...value.results];
      state.next = value.next;
      // release the lock
      state.waiting = false;
    }
  },
  actions: {
    async refresh_data({ commit }) {
      commit("commit_waiting");
      let ret = await axios.get("/v0/outbreaks/");
      commit("add_outbreaks", ret.data);

      return ret;
    }
  }
};
