CREATE TABLE articles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(100) NOT NULL,
content VARCHAR(200) NOT NULL,
createdAT DATE NOT NULL
);

PRAGMA table_info('articles');

INSERT INTO
  articles (title, content, createdAT)
VALUES
  ('hello', 'world', '2000-01-01'),
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

-- DATE함수 사용해서 데이터 입력
INSERT INTO
  articles (title, content, createdAT)
VALUES
  ('mytitle', 'mycontent', DATE());

-- 조회
SELECT
  *
FROM
  articles;

-- UPDATE / 레코드 수정
UPDATE
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

UPDATE
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

-- DELETE / 레코드 삭제
DELETE FROM
  articles
WHERE
  id = 1;

DELETE FROM
  articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAT
  LIMIT 2
);

-- 심화(서브쿼리)
-- 제일 최근에 생성된 게시글을 골라서 하나만 삭제

DELETE FROM
  articles
WHERE
  id IN (
    SELECT id
    FROM articles
    ORDER BY createdAT DESC
    LIMIT 1
);