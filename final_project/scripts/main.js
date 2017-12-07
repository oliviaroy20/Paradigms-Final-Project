Div.prototype = new Item()

labelTitle = new Label(); 
divLabelTitle = new Div(); 
divLabelTitle.createDiv("divLabelTitle"); 
labelTitle.createLabel("MexiComida", "titleLabel"); 
divLabelTitle.addItemToDiv(labelTitle); 
divLabelTitle.addToDocument();

label1 = new Label(); 
label1.createLabel("Where would you like to eat?", "label1")
div1 = new Div(); 
div1.createDiv("div1")
div1.addItemToDiv(label1)
div1.addToDocument(); 

dropdownCusine = new Dropdown(); 
//button to search for restaurant 
buttonSearch = new Button(); 
buttonSearch.createButton("Search", "buttonSearch"); 
//args = [dropdownCuisine, dropdownDressCode, dropdownPayment, dropdownPrice]
//buttonSearch.addClickEventHandler(searchHandler, args); 
////div for button 
divSearchButton = new Div()
divSearchButton.createDiv("divSearchButton");
divSearchButton.addItemToDiv(buttonSearch); 
divSearchButton.addToDocument(); 

divCuisine = new Div(); 
divCuisine.createDiv("divCuisine"); 
labelCuisine = new Label(); 
divLabelCuisine = new Div(); 
divLabelCuisine.createDiv("divLabelCuisine"); 
labelCuisine.createLabel("Cuisine: ", "cuisineLabel");
divLabelCuisine.addItemToDiv(labelCuisine); 
divCuisine.addItemToDiv(divLabelCuisine);

dropdownCuisine = new Dropdown(); 
divDropdownCuisine = new Div();
divDropdownCuisine.createDiv("divDropdownCuisine");
//add code for dropdown 
var xhr1 = new XMLHttpRequest(); 
xhr1.open("GET", "http://student04.cse.nd.edu:51067/cuisine/", true);
xhr1.onload= function(e){
	var dict1 = JSON.parse(xhr1.responseText); 
	dropdownCuisine.createDropdown(dict1.cuisines, "dropdownCuisine", "None");
	divDropdownCuisine.addItemToDiv(dropdownCuisine);
	divCuisine.addItemToDiv(divDropdownCuisine); 
	divCuisine.addToDocument();
}
xhr1.onerror = function(e){
	console.error(xhr1.statusText);
}
xhr1.send(null);

//total Dress code div
divDressCode = new Div(); 
divDressCode.createDiv("divDressCode");
//label for Dress code:
labelDressCode = new Label();
//div for the label for dress code 
divLabelDressCode = new Div(); 
divLabelDressCode.createDiv("divLabelDressCode");
labelDressCode.createLabel("Dress code: ", "dressCodeLabel");
divLabelDressCode.addItemToDiv(labelDressCode);
divDressCode.addItemToDiv(divLabelDressCode);

//dropdown for dress code 
dropdownDressCode = new Dropdown();
//var dict = ["informal", "casual", "None"]; 
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://student04.cse.nd.edu:51067/dresscode/", true);
xhr.onload = function(e){
	var dict = JSON.parse(xhr.responseText);
	dropdownDressCode.createDropdown(dict.dresscode, "dressCodeDropdown", "None"); 
//	dropdown div for dress code 
	divDropdownDressCode = new Div();
	divDropdownDressCode.createDiv("divDropdownDressCode");
	divDropdownDressCode.addItemToDiv(dropdownDressCode);
	//add div which contains drop down to the dress code div
	divDressCode.addItemToDiv(divDropdownDressCode);
	divDressCode.addToDocument();
};
xhr.onerror= function(e){
	console.error(xhr.statusText);
};
xhr.send(null); 

//div for Payment label and dropdown 
divPayment = new Div(); 
divPayment.createDiv("divPayment"); 

//label for payment
labelPayment = new Label();
//div for payment label
divLabelPayment = new Div(); 
divLabelPayment.createDiv("divLabelPayment");
labelPayment.createLabel("Payment Accepted: ", "paymentLabel"); 
divLabelPayment.addItemToDiv(labelPayment); 

//dropdown for payment
dropdownPayment = new Dropdown(); 
xhr2 = new XMLHttpRequest();
xhr2.open("GET", "http://student04.cse.nd.edu:51067/payments/", true); 
xhr2.onload = function(e){
	var dict2 = JSON.parse(xhr2.responseText);
	dropdownPayment.createDropdown(dict2.payment, "dropdownPayment", "None"); 
	//div for dropdown of Payment
	divDropdownPayment = new Div(); 
	divDropdownPayment.createDiv("divDropdownPayment"); 
	divDropdownPayment.addItemToDiv(dropdownPayment); 
	//add div which holds label and drop down to the overall payment div
	divPayment.addItemToDiv(divLabelPayment);
	divPayment.addItemToDiv(divDropdownPayment);
	divPayment.addToDocument(); 
}
xhr2.onerror = function(e){
	console.error(xhr2.statusText)
}
xhr2.send(null)
//div for overall Price 
divPrice = new Div()
divPrice.createDiv("divPrice"); 
//label for price
labelPrice = new Label();
//div for the price label  
divLabelPrice = new Div(); 
divLabelPrice.createDiv("divLabelPrice"); 
labelPrice.createLabel("Price: ", "priceLabel"); 
divLabelPrice.addItemToDiv(labelPrice);

//dropdown for Price 
dropdownPrice = new Dropdown(); 
xhr3 = new XMLHttpRequest();
xhr3.open("GET", "http://student04.cse.nd.edu:51067/prices/", true);
xhr3.onload = function(e){
	var dict3 = JSON.parse(xhr3.responseText); 
	dropdownPrice.createDropdown(dict3.price, "dropdownPrice", "None"); 
	//div for dropdown for price
	divDropdownPrice = new Div(); 
	divDropdownPrice.createDiv("divDropdownPrice");
	divDropdownPrice.addItemToDiv(dropdownPrice);
	//and div for dropdown and label to overall div and add to document
	divPrice.addItemToDiv(divLabelPrice); 
	divPrice.addItemToDiv(divDropdownPrice); 
	divPrice.addToDocument();
}
xhr3.onerror = function(e){
	console.error(xhr3.statusText)
}
xhr3.send(null)
//button to search for restaurant 

args = [dropdownCuisine, dropdownDressCode, dropdownPayment, dropdownPrice]
buttonSearch.addClickEventHandler(searchHandler, args); 

divResults = new Div()
divResults.createDiv("divResults");
divResults.addToDocument(); 
//post the filter results so it can do a get using them 
function searchHandler(args){
	var xhr = new XMLHttpRequest()
	var cuisine = args[0].getSelected()
	var dresscode = args[1].getSelected()
	var payment = args[2].getSelected()
	var price = args[3].getSelected()
	xhr.open("POST", "http://student04.cse.nd.edu:51067/recommendations/", true);
	var dict = {"Cuisine": cuisine, "Dress Code": dresscode, "Payment Accepted": payment, "Price": price} 
	xhr.onload = function(e){
		getRecommendation();
	}
	xhr.onerror = function(e){
		console.error(xhr.statusText)
	}
	xhr.send(JSON.stringify(dict))
}
//get recommendations and parse through results to make it look decent 
function getRecommendation(){
	var xhr = new XMLHttpRequest()
	xhr.open("GET", "http://student04.cse.nd.edu:51067/recommendations/", true); 
	xhr.onload = function(e){
		divResults.deleteAll(); 
		var results = JSON.parse(xhr.responseText)
		//console.log(results)	
		for (var key in results.recommendations){ 
			nameLabel = new Label()
		//	label.createLabel(JSON.stringify(results.recommendations[key]), "label")
			nameLabel.createLabel("Name: " + toTitleCase(results.recommendations[key]["Name"]), "label")
			divResults.addItemToDiv(nameLabel);
			cuisineLabel = new Label()
			cuisineLabel.createLabel("Cuisine: " +toTitleCase(results.recommendations[key]["Cuisine"]), "label")
			divResults.addItemToDiv(cuisineLabel);
			priceLabel = new Label(); 
			priceLabel.createLabel("Price: " + toTitleCase(results.recommendations[key]["Price"]), "label")
			divResults.addItemToDiv(priceLabel);
			paymentLabel = new Label()
			paymentLabel.createLabel("Payments Accepted: " + toTitleCase(results.recommendations[key]["Payment Accepted"]), "label")
			divResults.addItemToDiv(paymentLabel)
			dressCodeLabel = new Label()
			dressCodeLabel.createLabel("Dress Code: "+ toTitleCase(results.recommendations[key]["Dress Code"]) , "label")
			divResults.addItemToDiv(dressCodeLabel)
			ratingButton = new Button() 
			ratingButton.createButton("Ratings", "id" )
			args1 = [String( key) + "|" + toTitleCase(results.recommendations[key]["Name"])]
			ratingButton.addClickEventHandler(ratingsHandler,args1) 
	//		ratingButton.setOnClick("ratingPage.html")
			divResults.addItemToDiv(ratingButton)
			emptyLabel = new Label()
			emptyLabel.createLabel("----------------------------------", "label")
			divResults.addItemToDiv(emptyLabel)
		
		
		}
		divResults.addToDocument(); 
	}
	xhr.onerror = function(e){
		console.error(xhr.statusText); 
	}
	xhr.send(null) 
}

function toTitleCase(str)
{
	if (str==null){
	return "Not Available"
}
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}
//set the cookie to the id (which holds the id and name of a restaurant
function setCookie(id){
	document.cookie = "cookie =" + id ;
}
//set cookie and go to next page
function ratingsHandler(args1){	
	setCookie(args1[0]);
	location.href = "ratingPage.html"
	

}
