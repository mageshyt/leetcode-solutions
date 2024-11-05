class Solution {
public:
    bool isCircularSentence(string sentence) {
      int n=sentence.length();

      if (sentence[0] != sentence[n-1]) {
        return false;
      }

      for(int i=0;i<n-1;i++){
        // if there is a space and the next character is not the first character
        if(sentence[i]==' ' && sentence[i-1]!=sentence[i+1]){
          return false;
        }
      }

      return true;
        
    }
};
