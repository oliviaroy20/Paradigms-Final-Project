Div.prototype = new Item() 


//set up title, back butto and get current rating 
labelTitle = new Label();
divLabelTitle = new Div();
divLabelTitle.createDiv("divLabelTitle");
labelTitle.createLabel("MexiComida", "titleLabel");
divLabelTitle.addItemToDiv(labelTitle);
divLabelTitle.addToDocument();

divHome = new Div();
divHome.createDiv("divHome")
buttonHome = new Button();
buttonHome.createButton("Go back", "buttonHome")
buttonHome.setOnClick("index.html")
divHome.addItemToDiv(buttonHome)
divHome.addToDocument(); 

divRating = new Div();
divRating.createDiv("divRating");
divExplanation = new Div(); 
divExplanation.createDiv("divExp");
labelRating = new Label();
//get cookie, save it, and delete cookie
var cookie = readCookie("cookie")
console.log(cookie)
rid = cookie.split("|")[0]
name = cookie.split("|")[1]
document.cookie = "cookie=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
var xhr = new XMLHttpRequest();

xhr.open("GET", "http://student04.cse.nd.edu:51067/ratings/" + rid, true);
xhr.onload = function(e){

	var rating = JSON.parse(xhr.responseText)
	labelRating.createLabel("The rating for " + name + " is " + rating["rating"][0], "ratingText")
	divRating.addItemToDiv(labelRating); 
	divRating.addToDocument();
	rate()
}
xhr.onerror = function(e){
	console.error(xhr.statusText);
}
xhr.send(null)
//get a selected value and put rating 
function rate(){
	labelQ = new Label(); 
	labelQ.createLabel("What would you rate this restaurant? Add or change your vote!", "labelQ");
	divExplanation.addItemToDiv(labelQ); 
	dropRating = new Dropdown(); 
	var dict = ["Poor-0", "Average-1", "Great-2"]
	dropRating.createDropdown(dict, "dropRating", "Great-2" );
	divExplanation.addItemToDiv(dropRating);
	rateButton = new Button(); 
	rateButton.createButton("Rate!", "rateButton2")
	args = [dropRating]
	rateButton.addClickEventHandler(rateHandler, args); 
	divExplanation.addItemToDiv(rateButton); 
	divExplanation.addToDocument();  

}


//get the cookie and return the value 
function readCookie(name){
	var nameCookie = name +"=";
	var ca = document.cookie.split(';'); 
	for (var i =0; i<ca.length; i++){
		var c = ca[i];
		while(c.charAt(0) == ' '){
			c = c.substring(1);
		}
		if (c.indexOf(nameCookie) ==0){
			return c.substring(nameCookie.length, c.length); 
		}
	}
	return "";
}
//executes the put of the rating 
function rateHandler(args){
	var xhr1 = new XMLHttpRequest()
	var selected = args[0].getSelected()
	var rating = selected.split("-")[1]
	var data = {"uid": 1002, "rating" : [parseFloat(rating) , 0,0 ]}
	console.log(data["rating"])
	xhr1.open("PUT" , "http://student04.cse.nd.edu:51067/ratings/" +rid , true)
	xhr1.onload=  function(e){
		divExplanation.deleteAll()
		labelThanks = new Label(); 
		labelThanks.createLabel("Thank you for voting!")
		divExplanation.addItemToDiv(labelThanks);
		divExplanation.addToDocument();
		location.reload();		
	 
	};
	xhr1.onerror = function(e){
		console.error(xhr1.statusText); 
	};
	xhr1.send(JSON.stringify(data))

}

