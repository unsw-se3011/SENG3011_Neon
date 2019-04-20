"use strict";

import Vue from "vue";
import axios from "axios";

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
axios.defaults.headers.common["Authorization"] = localStorage.getItem("token");
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let config = {
  // baseURL: process.env.baseURL || process.env.apiUrl || ""
  baseURL:
    process.env.NODE_ENV === "production"
      ? "http://neon.whiteboard.house/v0/"
      : "/v0/"
  // timeout: 60 * 1000, // Timeout
  // withCredentials: true, // Check cross-site Access-Control
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
function createTokenRefreshIntercept() {
  const interceptor = _axios.interceptors.response.use(
    response => {
      // Do something with response data
      return response;
    },
    error => {
      // Do something with response error
      console.log(error.status);
      if (error.response.status !== 401) {
        return Promise.reject(error);
      }
      console.log("try to solve the expire");
      // eject this  interceptor to prevent loop
      // when some edge case
      _axios.interceptors.response.eject(interceptor);
      return _axios
        .post("/jwt_refresh/", {
          refresh_token: localStorage.getItem("token")
        })
        .then(response => {
          localStorage.setItem("token", "JWT " + response.data.token);
          // set the axios to the new item
          error.response.config.headers["Authorization"] =
            "JWT " + response.data.token;
          _axios.defaults.headers.common["Authorization"] =
            "JWT " + response.data.token;
          return _axios(error.response.config);
        })
        .catch(error => {
          localStorage.removeItem("token");
          // this line may not work
          this.router.push("/auth/login");
          return Promise.reject(error);
        })
        .finally(createTokenRefreshIntercept);
    }
  );
}
createTokenRefreshIntercept();

// crete the refresh interceptor by this funciton
Plugin.install = function(Vue) {
  Vue.axios = _axios;
  window.axios = _axios;
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      }
    },
    $axios: {
      get() {
        return _axios;
      }
    }
  });
};

Vue.use(Plugin);

export default Plugin;
