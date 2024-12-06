// Description: create a sql file with the following content
// create data for 'id, name, phone' and two contacts
// inline autocomplete works for the file: type `id` and press tab to autocomplete the header
// and `name` and `phone` to autocomplete the values

INSERT INTO contacts (id, name, phone)
VALUES (1, 'John Doe', '123-456-7890'),
    (2, 'Jane Smith', '987-654-3210');