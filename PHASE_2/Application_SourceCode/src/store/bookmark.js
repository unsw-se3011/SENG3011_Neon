function initial() {
  return {
    waiting: true,
    bookmarks: [],
    bookmark_ids: []
  };
}

export default {
  namespaced: true,
  state: initial(),
  mutations: {
    commit_waiting: state => {
      // reset the ramen id
      state.waiting = true;
      state.bookmarks = [];
    },
    set_bookmark: (state, value) => {
      // add the data array and pagination informations
      state.bookmarks = value;
      state.bookmark_ids = state.bookmarks.map(el => el.id);
      state.waiting = false;
    },
    push_bookmark: (state, val) => state.bookmark_ids.push(val),
    remove_bookmark: (state, val) => {
      state.bookmark_ids = state.bookmark_ids.filter(el => el != val);
    }
  },
  actions: {
    async refresh_data({ commit }) {
      if (!localStorage.getItem("token")) {
        // only the login one can have bookmark
        // nothing to fetch
        commit("set_bookmark", []);
        return;
      }
      commit("commit_waiting");
      let ret = await window.axios.get("/bookmark/");
      commit("set_bookmark", ret.data);
      return ret;
    },
    async add_bookmark({ commit, dispatch }, val) {
      commit("push_bookmark", val);
      let ret = await window.axios.post("/bookmark/", { report: val });
      // for backen and frontend integrity, we have to check it
      dispatch("refresh_data");
      return ret;
    },
    async del_bookmark({ commit, dispatch }, val) {
      commit("remove_bookmark", val);
      let ret = await window.axios.delete(`/bookmark/${val}`);

      // for backen and frontend integrity, we have to check it
      dispatch("refresh_data");
      return ret;
    },
    async toggle_bookmark({ state, dispatch }, val) {
      if (state.bookmark_ids.includes(val)) {
        // go off the report
        return await dispatch("del_bookmark", val);
      } else {
        return await dispatch("add_bookmark", val);
      }
    }
  }
};
