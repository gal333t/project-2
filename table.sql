CREATE TABLE users(id SERIAL PRIMARY KEY, username TEXT NOT NULL, user_pwd TEXT NOT NULL);
DROP TABLE users;

CREATE TABLE images(id SERIAL PRIMARY KEY, img_url TEXT NOT NULL, text_desc TEXT NOT NULL, img_year INTEGER NOT NULL);
DROP TABLE images;

CREATE TABLE messages(id SERIAL PRIMARY KEY, user_msg TEXT NOT NULL);
DROP TABLE messages;

INSERT INTO users(name, username, user_pwd) VALUES (%s, %s);



INSERT INTO images(name, img_url, text_desc, img_year) VALUES (%s, %s, %s);
<img src="https://i.ibb.co/yPSjJyX/c91ca8b9-eb4f-4521-a86e-04694a50f256.jpg"> 2022, Janine Ziva at someones 90th
<img src="https://i.ibb.co/NNVbbKm/H-D-Wedding-01605.jpg"> 2021 Hannah wedding me Gabi Ziva Hannah 
<img src="https://i.ibb.co/sj70p5F/H-D-Wedding-01242.jpg"> 2021 Hannah & Ziva
<img src="https://i.ibb.co/pntF5Kg/64914e03-6215-46b7-8ad8-fc1c9cf209f5.jpg"> 2019 Ziva Isa me
<img src="https://i.ibb.co/HKzsK9v/136df341-fd11-47af-a1dd-6c31704c39fd.jpg"> 2019 Ziva Fudge in trolley
<img src="https://i.ibb.co/Ks39Mgw/e0712f96-2b91-4ae3-94e9-42bcb50f3aec.jpg"> 2018 Ziva Joel Opera house
<img src="https://i.ibb.co/cDpgTSW/IMG-4820.jpg"> 2018 Ziva Granny me at airport
<img src="https://i.ibb.co/QrV3c4k/5aab7870-7a73-40bb-88eb-832693ff7568.jpg"> 2018 Ziva baby Ashi selfie
<img src="https://i.ibb.co/R4Kk1j9/IMG-4091.jpg"> 2015 my Graduation Ziva Joel me
<img src="https://i.ibb.co/KxmWQ4Q/54-CC02-E8-D493-4931-A6-D0-7-A3256-AB16-A0.jpg"> 2020 Ziva and I boat selfie
<img src="https://i.ibb.co/M7MVHwx/b91bd789-92e9-4760-ad6b-9e28319e026f.jpg"> 2023 Ziva Aurie
<img src="https://i.ibb.co/Mgj48xS/ziva-joel-on-couch.jpg"> 2019 ziva joel on couch
<img src="https://i.ibb.co/1f36gXg/ziva-granny.jpg"> 2020 ziva and granny
<img src="https://i.ibb.co/RhfQs16/kurr-fam.jpg"> 2022 kurr family ziva me liat
<img src="https://i.ibb.co/g7bVj6d/alon-ziva.jpg"> 2022 alon-ziva
<img src="https://i.ibb.co/NpdQcSh/ziva-baby-outfit.jpg"> 2023 ziva baby outfit
<img src="https://i.ibb.co/g6s6LdM/ziva-liat-vineyard.jpg"> 2020 ziva-liat-vineyard
<img src="https://i.ibb.co/5knpZ0r/fam-on-boat.jpg"> 2019 fam-on-boat
<img src="https://i.ibb.co/gDKRjc0/alons-barmi.jpg"> 2011 alons-barmi