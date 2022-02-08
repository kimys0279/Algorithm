var readlineSync = require ('readline-sync');
if (readlineSync.keyInYN('Do you want this module?')) {
    console.log('Installing now...');
} else {
    console.log('Searching another...');
}