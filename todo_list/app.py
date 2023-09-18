from flask import Flask, render_template, request, redirect, url_for, request

app = Flask(__name__, template_folder='templates')