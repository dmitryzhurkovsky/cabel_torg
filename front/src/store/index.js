import { createStore } from 'vuex'
import auth from "./auth.js";
import header from "./header.js";
import notification from "./notification.js";
import breadcrumb from "./breadcrumb.js";
import profile from "./profile.js";
import order from "./order.js";

export default createStore({

  modules: {
    auth          : auth,
    header        : header,
    notification  : notification,
    breadcrumb    : breadcrumb,
    profile       : profile,
    order         : order,
  }
})
