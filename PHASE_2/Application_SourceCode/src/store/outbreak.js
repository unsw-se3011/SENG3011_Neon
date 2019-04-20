function initial() {
  return {
    waiting: true,
    outbreaks: []
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
      let ret = await window.axios.get("/outbreaks/");
      commit("add_outbreaks", ret.data);
      return ret;
    },
    async get_detail(state, id) {
      let p = await Promise.all([
        window.axios.get("/outbreaks/" + id),
        window.axios.get(`/outbreaks/${id}/chart/`)
      ]);
      // merge two request together
      let ret = p[0];
      ret.data.chart = p[1].data;
      // console.log(ret);
      return ret;
    }
  }
};
