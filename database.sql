BEGIN;
--
-- Create model SignsVector
--
CREATE TABLE "demoapp_signsvector" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "userID" integer NOT NULL, "sign1" integer NOT NULL, "sign2" integer NOT NULL, "sign3" integer NOT NULL, "sign4" integer NOT NULL);
COMMIT;
