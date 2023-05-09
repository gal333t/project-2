CREATE TABLE users(id SERIAL PRIMARY KEY, username TEXT NOT NULL, user_pwd TEXT NOT NULL);
DROP TABLE users;

CREATE TABLE images(id SERIAL PRIMARY KEY, img_url TEXT NOT NULL, text_desc TEXT NOT NULL, img_year INTEGER NOT NULL);
DROP TABLE images;

CREATE TABLE messages(id SERIAL PRIMARY KEY, username TEXT NOT NULL, user_msg TEXT NOT NULL);
DROP TABLE messages;

INSERT INTO users(username, user_pwd) VALUES (%s, %s);

INSERT INTO messages(username, user_msg) VALUES('Galit', 'Mom, you are the glue that holds our family together, the sunshine on a cloudy day, and the chocolate chips in our cookies!');

INSERT INTO images(img_url, text_desc, img_year) VALUES (%s, %s, %s);