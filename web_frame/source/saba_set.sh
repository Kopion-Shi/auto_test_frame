pwd

sudo setenforce 0

#防火墙（firewalld）开放 samba 服务
sudo firewall-cmd --permanent --add-service=samba
sudo firewall-cmd --reload
sudo systemctl restart firewalld
#设置 smb 服务
sudo systemctl start smb
sudo systemctl enable smb

echo 'over'

##启动docker
docker start jenkins
docker start mysql

##启动movie_web
cd /date/movie_web
conda activate pro_movie
python manage.py runserver 0.0.0.0:8000

##启动nginx
/usr/local/nginx/sbin/nginx

