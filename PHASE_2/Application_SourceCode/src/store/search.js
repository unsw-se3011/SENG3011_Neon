/**
 * This is for attach the standard seng apis and provide the search
 * functionality with it
 */

export default {
  namespaced: true,

  state: {
    filter_show: false,
    search_key: "",
    start_date: "",
    end_date: ""
  },
  mutations: {
    toggle_filter: ({ state }) => {
      // toggle the show boolean
      state.filter_show = !state.filter_show;
    }
  },
  actions: {
    refresh_data: ({ commit }) => {
      // should fetch two database
    }
  }
};
