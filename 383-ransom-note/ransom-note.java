class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> dictionary = new HashMap<>();

        for(Character c: magazine.toCharArray()) {
            dictionary.put(c, dictionary.getOrDefault(c, 0) + 1);
        }
        // System.out.println(dictionary);
        for(Character c: ransomNote.toCharArray()) {
            if(dictionary.containsKey(c) && dictionary.get(c) > 0){
                dictionary.put(c, dictionary.get(c)-1);
            }
            else {
                return false;
            }
        }
        return true;
    }
}
