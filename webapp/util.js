/**
 * Just some utility functions that can be used generically in lots of other js webapps.
 * Main one is callAPIGetJson to query an API and return the JSON response.
 */

 /**
  * Call an API with a GET and return the JSON response. Run with hardcoded retry count.
  * So
  * @param  {String} actualUrl The url to query for the JSON response
  * @return {Object}           json object with response
  */
 async function callAPIGetJson(actualUrl) {
   var retryCount = 5;
   const json = await fetchRetry(actualUrl, { method: 'GET' }, retryCount)
     .then((response) => {
       if (!response.ok) {
         throw new Error('Unknown error encountered querying API at URL: ' + actualUrl);
       }
       return response.json();
     })
     .catch(function(error) {
       console.error('error:', error);
       return error;
     });
   console.log(json);
   return json;
 };

 /**
  * Fetch from an API with retry logic when there are errors.
  * @param  {String} url     The url to query
  * @param  {String} options Key/Value pair of options to use in the request
  * @param  {String} n       The number of times to retry a failed API call
  * @return {Object}         json object with response
  */
 async function fetchRetry(url, options, n) {
     console.log("Fetch attempt: " + n);
     try {
         return await fetch(url, options);
     } catch(err) {
         if (n === 1) {
           console.log("Fetch failed: Throwing an exception");
           throw err;
         }
         console.log("Fetch failed: sleeping and retrying");
         var sleepSeconds = 60;
         await sleep(sleepSeconds * 1000);
         return await fetchRetry(url, options, n - 1);
     }
 };

 /**
  * Sleep function
  * @param  {Integer} ms Sleep for this many milliseconds
  * @return None
  */
 function sleep(ms) {
     console.log('Sleeping for milliseconds: ' + ms);
     return new Promise(resolve => setTimeout(resolve, ms))
 };
