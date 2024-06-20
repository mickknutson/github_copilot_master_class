public class HandyDictionaryTests {
    
    void testHandyDictionary(){
        HandyDictionary dictionary = new HandyDictionary();
        dictionary.add("apple", "사과");
        dictionary.add("banana", "바나나");
        dictionary.add("cherry", "체리");
        dictionary.add("date", "날짜");
        dictionary.add("date", "데이트");
        
        String result = dictionary.find("apple");
        System.out.println(result);
        result = dictionary.find("banana");
        System.out.println(result);
        result = dictionary.find("cherry");
        System.out.println(result);
        result = dictionary.find("date");
        System.out.println(result);

        // Assettions

        result = dictionary.find("cherry");
        System.out.println(result);
        result = dictionary.find("date");
        System.out.println(result);

        // Assettions
    }
}
