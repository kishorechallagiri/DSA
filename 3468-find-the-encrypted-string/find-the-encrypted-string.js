/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var getEncryptedString = function(s, k) {
   let newStr = "";
   for(let i=0;i<s.length;i++){
     newStr = newStr + s[(i+k) % s.length]
   };
   return newStr;
};