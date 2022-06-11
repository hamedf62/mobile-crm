// import Vue from 'vue'

import moment from "moment-jalaali";
moment.loadPersian({ dialect: "persian-modern" });

export default (ctx, inject) => {
  ctx.$moment = moment;
  inject("moment", moment);
};
