FROM nginx:stable
COPY default.conf /etc/nginx/conf.d
CMD sudo ufw allow 'Nginx Full' && sudo ufw allow OpenSSH && sudo ufw enable