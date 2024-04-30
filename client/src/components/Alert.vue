<template>
   <div>
    <b-alert variant="success" show>{{ message }}    <button type="button" @click="cancel()">x</button> </b-alert>

    <br>
  </div>
</template>

<script>
export default {
  /****
   * 在Vue.js组件中，name属性是可选的，可以省略。
   *
   * name属性用于标识当前组件的名称，可以在调试工具中使用。如果省略了name属性，Vue.js会自动为组件设置一个默认的名称，这个名称通常是由组件的文件名来推断出来的。
   *
   * 如果你不需要在调试工具中查看当前组件的名称，那么可以省略name属性。但是如果你需要在组件中使用自定义指令、
   * 过滤器、混入等高级功能，那么最好给组件设置一个明确的name属性，以便于在这些高级功能中使用。
   *
   * 总之，name属性是可选的，如果你不需要使用调试工具或高级功能，可以省略它，Vue.js会自动为你生成一个默认的名称。
   ***/
  // name: "Alert",
  props:['message'],
  methods:{
    cancel(){
      console.log('关闭子组件');
      this.$emit("closed");
    //  $emit 当前组件
    }
  },
};
</script>

<style scoped>

</style>
