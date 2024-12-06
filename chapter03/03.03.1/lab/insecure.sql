//

public void getUserData(String userId) {
    String query = "SELECT * FROM users WHERE userId = '" + userId + "'";
    executeQuery(query);
}


-- public void getUserData(String userId) {
--     String query = "SELECT * FROM users WHERE userId = ?";
--     try (PreparedStatement stmt = connection.prepareStatement(query)) {
--         stmt.setString(1, userId);
--         ResultSet rs = stmt.executeQuery();
--         // Process the result set
--     } catch (SQLException e) {
--         // Handle SQL exception
--     }
-- }