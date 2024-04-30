// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';

//导入bootstrap
import 'bootstrap/dist/css/bootstrap.css';
//导入 bootstrap vue库
import BootstrapVue from 'bootstrap-vue'

Vue.config.productionTip = false;

//启用 BootstrapVue库
Vue.use(BootstrapVue);
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
//  所有根節點的 template
});
