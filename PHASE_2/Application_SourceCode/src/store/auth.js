import Router from "vue-router";

function initial() {
  return {
    id: localStorage.getItem("uid"),
    username: localStorage.getItem("username") || "",
    first_name: localStorage.getItem("first_name") || "",
    last_name: localStorage.getItem("last_name") || "",
    auth_expire: localStorage.getItem("auth_expire") || ""
  };
}

export default {
  namespaced: true,
  state: initial,
  mutations: {
    ADD_TOKEN: (state, token) => {
      // store this token to local storage
      // with 4.5 minutes of expire
      let expire = new Date().getTime() + 270000;
      localStorage.setItem("token", token);
      localStorage.setItem("expire", expire);
      state.token = token;
      state.expire = expire;
    },
    ADD_USER: (state, { username, first_name, last_name, id }) => {
      // store the username in localstorage
      localStorage.setItem("username", username);
      localStorage.setItem("first_name", first_name);
      localStorage.setItem("last_name", last_name);
      localStorage.setItem("uid", id);
      state.username = username;
      state.first_name = first_name;
      state.last_name = last_name;
      state.id = id;
    },
    RESET: state => {
      // remove all the state in localstorage
      localStorage.clear();
      // remove the axios record
      window.axios.defaults.headers.common["Authorization"] = null;
      const s = initial();
      Object.keys(s).forEach(key => {
        state[key] = s[key];
      });
    }
  },
  actions: {
    async loginByCredential({ commit, state, dispatch }, credential) {
      let res;
      try {
        res = await window.axios.post("/jwt/", credential);
        // add this token to store
        // modify the auth type
        commit("ADD_TOKEN", "JWT " + res.data.token);
        // use this token to do axios request
        window.axios.defaults.headers.common["Authorization"] = state.token;
      } catch (error) {
        // logout
        Router.push("/auth/login");
      }
      // fetch the user detail into frontend
      dispatch("getUserDetail");

      // return back this promise back to support chaining
      return res;
    },
    async registerByUser({ dispatch }, user) {
      await window.axios.post("/users/", user);
      dispatch("loginByCredential", {
        username: user.username,
        password: user.password
      });
    },
    async refreshToken({ state, commit }) {
      if (state.expire != "" && state.expire < new Date().getTime()) {
        // the token is exprie, we fetch a new token
        let ret = await window.axios.post("/jwt_refresh/", {
          token: state.token
        });
        commit("ADD_TOKEN", "JWT " + ret.data.token);
        return ret;
      }
    },
    async editUser(state, user) {
      let ret = await window.axios.put(`/users/${user.id}/`, user);
      return ret;
    },
    async getUserDetail({ commit }) {
      let ret = await window.axios.get("/users/");
      commit("ADD_USER", ret.data);
      return ret;
    }
  }
};
