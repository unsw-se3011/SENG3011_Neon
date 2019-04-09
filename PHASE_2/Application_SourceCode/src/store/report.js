/**
 * Flat vuex, support decouple api calling
 */

import axios from "axios";

export default {
  namespaced: true,
  actions: {
    get_neon_report: (state, id) => axios.get(`/reports/${id}/`)
  }
};
