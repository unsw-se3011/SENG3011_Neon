<template>
  <div></div>
</template>
<script>
// fake component just do logout
export default {
  mounted() {
    this.$store.commit("auth/RESET");
    this.$router.push({ name: "login" });
  }
};
</script>
