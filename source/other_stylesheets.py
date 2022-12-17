CHECK_BOX_STYLESHEET = """
QCheckBox {
	font-family: Verdana, Geneva, sans-serif;
    font-size: 20px;
    letter-spacing: 2px;
    word-spacing: 6px;
    color: #a4978e;
}
QCheckBox:checked {
	color: #be9063;
	font: 75 20pt "Verdana";
	text-decoration: underline;
}
QCheckBox::indicator {
	background-color: #132226;
	border-radius: 5px;
}
QCheckBox::indicator:checked {
	background-color: #be9063;
}
"""