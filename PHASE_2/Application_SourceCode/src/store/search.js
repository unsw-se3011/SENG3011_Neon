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
    end_date: toDate(date_now)
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
    set_end_date: (state, value) => (state.end_date = value)
  },
  actions: {
    refresh_data: ({ commit }) => {
      // should fetch two database
    }
  }
};
