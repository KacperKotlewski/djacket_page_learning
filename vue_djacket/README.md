# vue_djacket

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


### Custom IP/URL for backend server API requests
create .env file in this directory (vue_djacket)

in file create line:
```env
VUE_APP_AXIOS_ADDRESS={http/https}://{IP}:{PORT}
```
example:
```env
VUE_APP_AXIOS_ADDRESS=http://127.0.0.1:8081
```