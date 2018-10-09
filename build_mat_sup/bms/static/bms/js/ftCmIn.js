function myForm(form) {
	var ft = Math.abs(form.ft.value);
	var inCm = Math.abs(form.inCm.value);
	/*if (ft <= 0) {
		var formula = inCm *2.54;
		var answer = Math.round(formula*10)/10;
		form.answer.value = answer;
	}
	else if  (form.inCm.value == "") {
		var formula = ft * 12 * 2.54;
		var answer = Math.round(formula*10)/10;
		var inch = Math.round((ft*12)*10)/10;
		form.answer.value = answer;
	}
	else {*/
		/*var eft = eval(ft);
		var eInCm = eval(inCm);*/
		var formula = (ft*12 + inCm)*2.54;
		var answer = Math.round(formula*10)/10;
		/*var inch = Math.round((ft*12)*10)/10 + inCm;*/
		form.answer.value = answer;
	/*return form.answer.value;*/
}
