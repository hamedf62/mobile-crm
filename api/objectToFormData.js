// import isEmpty from 'lodash/isEmpty'

const objectToFormData = (obj, form, namespace) => {
  const fd = form || new FormData()
  // console.log('obj in formdata', obj)
  for (const property in obj) {
    if (!Object.prototype.hasOwnProperty.call(obj, property)) {
      continue
    }

    const formKey = namespace ? `${namespace}[${property}]` : property

    if (obj[property] === null) {
      continue
    }
    // console.log(
    //   'obj[property]',
    //   obj[property],
    //   typeof obj[property],
    //   isEmpty(obj[property]),
    //   formKey
    // )
    if (typeof obj[property] === 'boolean') {
      fd.append(formKey, obj[property] ? '1' : '0')
      continue
    }
    //  || isEmpty(obj[property])
    if (typeof obj[property] === 'undefined') {
      continue
    }

    if (obj[property] != null) {
      if (typeof obj[property] === 'object') {
        // console.log(formKey, ))
        let passfilearray = false
        for (let i = 0; i < obj[property].length; i++) {
          const file = obj[property][i]
          if (file instanceof File) {
            passfilearray = true
            fd.append(formKey, file)
          }
        }
        if (passfilearray === true) {
          continue
        }
      }
    }

    if (typeof obj[property] === 'object' && !(obj[property] instanceof File)) {
      fd.append(formKey, JSON.stringify(obj[property]))
      continue
    }

    fd.append(formKey, obj[property])
  }

  return fd
}

export default objectToFormData
