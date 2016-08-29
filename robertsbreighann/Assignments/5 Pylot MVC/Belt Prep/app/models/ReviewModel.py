from system.core.model import Model

class ReviewModel(Model):
    def __init__(self):
        super(ReviewModel, self).__init__()


    def add_review(self, data):
        query = "INSERT INTO review (review, rating, user_id, book_id) "
        query += "VALUES (:review, :rating, :user_id, :book_id);"

        review_id = self.db.query_db(query, data)

        if review_id <= 0:
            return None

        return review_id

    def get_recent(self):
        query = "SELECT r.review, r.rating, r.user_id, r.book_id, r.created_at, review_user.alias, review_book.title "
        query += " FROM review r "
        query += " INNER JOIN user AS review_user ON r.user_id = review_user.id "
        query += " INNER JOIN book AS review_book ON r.book_id = review_book.id "
        query += " ORDER BY r.created_at DESC LIMIT 3;"
        return self.db.query_db(query)
