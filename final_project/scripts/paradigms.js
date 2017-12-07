function Item(){
	this.addToDocument = function(){document.body.appendChild(this.item);}
}

function Div(){
	this.createDiv = function(id){
		this.item = document.createElement("div")
		this.item.setAttribute("id", id); 
	};
	this.addItemToDiv = function(item2){
		this.item.appendChild(item2.item);
	};
	this.deleteAll = function(){
		while(this.item.firstChild){
			this.item.removeChild(this.item.firstChild)
		}
	};

}
function Label(){
	this.createLabel = function(text, id){
		this.item= document.createElement("p");
		var  text = document.createTextNode(text); 
		this.item.setAttribute("id", id);
		this.item.appendChild(text); 
	}; 
	this.setText = function(text){this.item.innerHTML = text;}; 
}

function Dropdown(){
	this.createDropdown = function(dict, id, selected){
		this.item= document.createElement("form")
		select = document.createElement("select")
		select.setAttribute("name", id)
		this.id = id 

		for (var x in dict){
			var tmp = document.createElement("option")
			tmp.setAttribute("id", id)
			tmp.setAttribute("value", dict[x])
			if ( dict[x]  == selected){
				tmp.selected = true
			}
			tmp.innerHTML = dict[x]
			select.append(tmp)
		}
		this.item.appendChild(select);
	};

	this.getSelected = function(){
		var choices = this.item.elements[this.id]
		for (var i =0; i<choices.length; i++){
			if (choices[i].selected) return choices[i].value
		}
		return 'error'
	};
}
function Button(){
	this.createButton = function(text, id){
		this.item = document.createElement("button");
		var text = document.createTextNode(text);
		this.item.setAttribute("id", id);
		this.item.appendChild(text);}; 
	this.addClickEventHandler = function(handler, args){
		this.item.onmouseup = function(){handler(args);};};

	this.setOnClick = function(link){
		this.item.onclick = function(e){
			location.href = link;
		} ;
	};
}


