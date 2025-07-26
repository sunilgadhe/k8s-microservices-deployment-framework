#!/bin/sh
cat <<EOF > /usr/share/nginx/html/env.js
window._env_ = {
  API_URL: "${API_URL}"
};
EOF

exec nginx -g 'daemon off;'
