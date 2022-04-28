from constants import C_ADMIN_PAGE_RECORDS_LIMIT


class PagePaginationService(object):

    previous_page = 0
    next_page = 0
    higher_limit = 0
    lower_limit = 0
    higher_limit_display = 0

    def __init__(self, total_records, page):
        self.total_records = total_records
        self.page = page
        self.previous_page = self.get_previous_page()
        self.next_page = self.get_next_page()
        self.higher_limit = self.get_higher_limit()
        self.higher_limit_display = self.get_higher_limit_display()
        self.lower_limit = self.get_lower_limit()

    def get_page(self):
        return self.page

    def get_previous_page(self):
        return self.page - 1

    def get_next_page(self):

        if self.page > 1 and self.total_records <= self.get_higher_limit():
            return 0

        return self.page + 1

    def get_higher_limit(self):
        return self.page * C_ADMIN_PAGE_RECORDS_LIMIT

    def get_higher_limit_display(self):
        if self.total_records < self.get_higher_limit():
            return self.total_records

        return self.page * C_ADMIN_PAGE_RECORDS_LIMIT

    def get_lower_limit(self):
        return (self.get_higher_limit() - C_ADMIN_PAGE_RECORDS_LIMIT) + 1

    def get_total_records(self):
        return self.total_records

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'total_records': self.total_records,
            'page': self.page,
            'previous_page': self.previous_page,
            'next_page': self.next_page,
            'higher_limit': self.higher_limit_display,
            'lower_limit': self.lower_limit
        }


def main():
    pass


if __name__ == "__main__":
    main()
