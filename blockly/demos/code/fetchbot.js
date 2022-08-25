Blockly.Blocks['fetchbot_move'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_MOVE"])
        .appendField(new Blockly.FieldDropdown([[Blockly.Msg["FETCHBOT_MOVE_FORWARD"],"forward"], [Blockly.Msg["FETCHBOT_MOVE_BACKWARD"],"backward"], [Blockly.Msg["FETCHBOT_MOVE_LEFT"],"left"], [Blockly.Msg["FETCHBOT_MOVE_RIGHT"],"right"]]), "fetchbot_mouvement_field")
        //.appendField(Blockly.Msg["FETCHBOT_MOVE_SPEED"])
        //.appendField(new Blockly.FieldNumber(0.5), "speed")
        //.appendField(Blockly.Msg["FETCHBOT_MOVE_DURATION"])
        //.appendField(new Blockly.FieldNumber(1), "duration")
        //.appendField(Blockly.Msg["FETCHBOT_SECONDS"]);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['fetchbot_move'] = function(block) {
  var dropdown_fetchbot_mouvement = block.getFieldValue('fetchbot_mouvement_field');
  //var motor_speed = block.getFieldValue('speed')
  //var duration = block.getFieldValue('duration')
  var code = "fetchbot.move(\"" + dropdown_fetchbot_mouvement + "\")\n";
  return code;
};



Blockly.Blocks['fetchbot_wait'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_WAIT"])
        .appendField(new Blockly.FieldNumber(1, 0), "fetchbot_wait_field")
        .appendField(Blockly.Msg["FETCHBOT_SECONDS"]);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['fetchbot_wait'] = function(block) {
  var code = "time.sleep(" + block.getFieldValue('fetchbot_wait_field') + ")\n";
  return code;
};


Blockly.Blocks['fetchbot_start_detection'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_START_CAMERA_DETECTION"]);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['fetchbot_detected_class'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_DETECTED_CLASS"]);
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['fetchbot_detected_class'] = function(block) {
  var code = "fetchbot.predict()";
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['fetchbot_message'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_MESSAGE"])
        .appendField(new Blockly.FieldTextInput(Blockly.Msg["FETCHBOT_MESSAGE_HELLO"]), "fetchbot_message_field");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['fetchbot_message'] = function(block) {
  var fetchbot_message = block.getFieldValue('fetchbot_message_field');
  var code = "fetchbot.say(\"" + fetchbot_message + "\")\n";
  return code;
};