


var devices = (function() {

   this.deviceList = {"items": {"sdk4": ["Ionic", "Versa", "Versa Lite", "Versa 2" ],
           "sdk5": ["Versa 3", "Sense"]
		  }
   };
    this.get = function() {
		
		return this.deviceList;

    };

    return this;
}());