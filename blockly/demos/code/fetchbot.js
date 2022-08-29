Blockly.Blocks['fetchbot_move'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_MOVE"])
        .appendField(new Blockly.FieldDropdown([[Blockly.Msg["FETCHBOT_MOVE_FORWARD"],"forward"], [Blockly.Msg["FETCHBOT_MOVE_BACKWARD"],"backward"], [Blockly.Msg["FETCHBOT_MOVE_LEFT"],"left"], [Blockly.Msg["FETCHBOT_MOVE_RIGHT"],"right"]]), "fetchbot_mouvement_field");
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
  return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['fetchbot_message'] = {
  init: function() {
    this.appendValueInput("message")
        .setCheck(null)
        .appendField(Blockly.Msg["FETCHBOT_MESSAGE"]);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


Blockly.Python['fetchbot_message'] = function(block) {
  var fetchbot_message = Blockly.Python.valueToCode(block, 'message', Blockly.Python.ORDER_NONE);
  var code = "fetchbot.say(" + fetchbot_message + ")\n";
  return code;
};

Blockly.Blocks['fetchbot_score'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(Blockly.Msg["FETCHBOT_SCORE"])
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['fetchbot_score'] = function(block) {
  var code = "fetchbot.score()";
  return [code, Blockly.Python.ORDER_NONE];
};