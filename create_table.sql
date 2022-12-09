CREATE TABLE "ratings" (
  "rating_id" int NOT NULL AUTO_INCREMENT,
  "IPAddress" varchar(45) NOT NULL,
  "Rating" int NOT NULL,
  "URL" varchar(255) NOT NULL,
  "rated" datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY ("rating_id")
);
