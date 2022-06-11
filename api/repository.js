// Provide nuxt-axios instance to use same configuration across the whole project
// I've used typical CRUD method names and actions here

import objectToFormData from "./objectToFormData";

export default ($axios, $store, $swal, i18n) => (resource) => ({
  index(params) {
    // console.log(params)
    let req_params = {};
    if (params) {
      req_params = { params: { params } };
    }
    return $axios.$get(`${resource}`, req_params);
  },

  show(id, params) {
    return $axios.$get(`${resource}/${id}`, {
      params: {
        params,
        // timestamp: new Date().getTime(),
      },
    });
  },

  create(payload, customRoute = "") {
    if (payload.data) {
      payload = objectToFormData(payload.data);
    }
    // payload.timestamp = new Date().getTime()
    return $axios.$post(`${resource}${customRoute}`, payload);
  },

  update(id, payload) {
    if (payload.data) {
      payload = objectToFormData(payload.data);
    }

    return $axios.$patch(`${resource}/${id}`, payload);
  },

  async delete(id, confirm = false) {
    // console.log(i18n)
    await $axios
      .$delete(`${resource}/${id}`, {
        params: {
          confirm: confirm,
        },
      })
      .then(async (response) => {
        await $swal
          .fire({
            title: i18n.t(response.meta.message.text),
            // imageUrl: '/img/Loader.gif',
            icon: "warning",
            // showDenyButton: true,
            showCancelButton: true,
            confirmButtonColor: response.meta.message.color ? response.meta.message.color : "red",
            confirmButtonText: i18n.t(response.meta.message.action),
            // denyButtonText: i18n.t(`Don't Delete`),
            cancelButtonText: i18n.t(`actions.cancel`),
          })
          .then(async (result) => {
            if (result.isConfirmed) {
              await $axios.$delete(`${resource}/${id}`, {
                params: {
                  confirm: true,
                },
              });
              // app.$swal.fire('Saved!', '', 'success')
            }
            // else if (result.isDenied) {

            //   // app.$swal.fire('Changes are not saved', '', 'info')
            //   // throw new Cancel()
            // }
          });
      });

    // return
  },

  getTree(params) {
    return $axios.$get(`${resource}/getTree`, {
      params: {
        params,
      },
    });
  },
  moveNode(params) {
    return $axios.$patch(`${resource}/${params.source.id}/move`, {
      // params: {
      parent_id: params.destination ? params.destination.id : null,
      position: params.position,
      // },
    });
  },
  getNodes(params) {
    return $axios.$get(`${resource}/getNodes`, {
      params: {
        params,
      },
    });
  },
});
