/**
 * Flat vuex, support decouple api calling
 */

const news_key = "62353b10678448e0b9a20d3f89dd3fb8";

export default {
  namespaced: true,
  actions: {
    get_neon_report: (state, id) => window.axios.get(`/reports/${id}/`),
    get_relate_news: (state, event) =>
      window.axios.get("https://newsapi.org/v2/everything", {
        params: {
          q: event.q,
          from: event.from,
          to: event.to,
          apiKey: news_key
        }
      })
  }
};
