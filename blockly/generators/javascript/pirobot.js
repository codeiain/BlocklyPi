Blockly.JavaScript['robot_motor_power'] = function (block) {
	var value_power = Blockly.JavaScript.valueToCode(block, 'POWER',
		Blockly.JavaScript.ORDER_ATOMIC);
	var dropdown_motor = block.getFieldValue('MOTOR');


	// Check the input ...
	if (value_power > 100) {
		alert("Maximum motor power for the robot is 100.");
		return '';
	}
	if (value_power < -100) {
		alert("Minimum motor power for the robot is 100.");
		return '';
	}

	// Generate the code ...
	var code = 'runPiRobotCommand("setRobotMotorPower", "' + dropdown_motor + '",' + value_power + ');';
	return code;
};

Blockly.JavaScript['robot_sleep'] = function (block) {
	var value_sleep = Blockly.JavaScript.valueToCode(block, 'SLEEP',
		Blockly.JavaScript.ORDER_ATOMIC);
	// Generate the code ...

	var code = 'runPiRobotCommand("setRobotSleep", ' + value_sleep + ');';
	return code;
};


Blockly.JavaScript['robot_switch_settings'] = function (block) {
	let port = block.getFieldValue('PORT');
	let value = Blockly.JavaScript.valueToCode(block, 'ONOFF',
		Blockly.JavaScript.ORDER_ATOMIC);
	value = value.replace(/'/g, '')
	let portcode = 0;

	if (port == 'ONE') {
		portcode = 1
	}
	if (port == 'TWO') {
		portcode = 2
	}
	if (port == 'THREE') {
		portcode = 3
	}

	var code = 'runPiRobotCommand("setRobotSwitch", "' + portcode + '",' + value + ');';
	return code;
}


Blockly.JavaScript['control_key_down'] = function (block) {
	// The inputs ...
	var statements_statements = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
	var dropdown_key = block.getFieldValue('KEY');
	var dropdown_type = block.getFieldValue('TYPE');

	// Determine the key code to listen for.
	var keyCode = 0;
	if (dropdown_key === 'UP') {
		keyCode = 38;
	} else if (dropdown_key === 'DOWN') {
		keyCode = 40;
	} else if (dropdown_key === 'RIGHT') {
		keyCode = 39;
	} else if (dropdown_key === 'LEFT') {
		keyCode = 37;
	} else {
		return '';
	}

	// Determine the type of event to listen to.
	var type = "keydown";
	if (dropdown_type === 'UP') {
		type = "keyup";
	} else if (dropdown_type === 'DOWN') {
		type = "keydown";
	} else {
		return '';
	}

	// Generate the code for the callback (using only keyCode an charCode).
	var callbackCode = 'var code = keyCode; if (charCode && code == 0) {code = charCode;}; if (code ===' + keyCode + ') {' + statements_statements + '}';
	callbackCode = callbackCode.replace(/\n/g, "\\n");
	callbackCode = callbackCode.replace(/["]+/g, "\\\"");

	// Assemble JavaScript into code variable.
	var code = 'window.addKeyEventListenerForBlock("' + block.id + '", "' + type + '", "' + callbackCode + '");';
	return code;
};