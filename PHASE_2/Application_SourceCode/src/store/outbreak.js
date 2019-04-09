function initial() {
  return {
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
  state: initial()
};
