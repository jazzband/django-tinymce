/**
 * Based on "TinyMCE Compressor PHP" from MoxieCode.
 *
 * http://tinymce.moxiecode.com/
 *
 * Copyright (c) 2008 Jason Davies
 * Licensed under the terms of the MIT License (see LICENSE.txt)
 *
 * Usage: copy this file into the same directory as tiny_mce.js and change
 * settings.page_name below to match your tinymce installation as appropriate.
 */
var tinyMCE_GZ = {
	settings : {
		themes : '',
		plugins : '',
		languages : '',
		disk_cache : true,
		page_name : '{% url tinymce-compressor %}',
		debug : false,
		suffix : ''
	},

	init : function(s, cb, sc) {
		var t = this, n, i;//, nl = document.getElementsByTagName('script');

		for (n in s)
			t.settings[n] = s[n];

		s = t.settings;

		t.baseURL = '{{ base_url }}';

		if (!t.coreLoaded)
			t.loadScripts(1, s.themes, s.plugins, s.languages, cb, sc);
	},

	loadScripts : function(co, th, pl, la, cb, sc) {
		var t = this, x, w = window, q, c = 0, ti, s = t.settings;

		function get(s) {
			x = 0;

			try {
				x = new ActiveXObject(s);
			} catch (s) {
			}

			return x;
		};

		// Build query string
		q = 'js=true&diskcache=' + (s.disk_cache ? 'true' : 'false') + '&core=' + (co ? 'true' : 'false') + '&suffix=' + escape(s.suffix) + '&themes=' + escape(th) + '&plugins=' + escape(pl) + '&languages=' + escape(la);

		if (co)
			t.coreLoaded = 1;

		// Send request
		x = w.XMLHttpRequest ? new XMLHttpRequest() : get('Msxml2.XMLHTTP') || get('Microsoft.XMLHTTP');
		x.overrideMimeType && x.overrideMimeType('text/javascript');
		x.open('GET', s.page_name + '?' + q, !!cb);
//		x.setRequestHeader('Content-Type', 'text/javascript');
		x.send('');

		// Handle asyncronous loading
		if (cb) {
			// Wait for response
			ti = w.setInterval(function() {
				if (x.readyState == 4 || c++ > 10000) {
					w.clearInterval(ti);

					if (c < 10000 && x.status == 200) {
						t.loaded = 1;
						t.eval(x.responseText);
						cb.call(sc || t, x);
					}

					ti = x = null;
				}
			}, 10);
		} else
			t.eval(x.responseText);
	},

	start : function() {
		var t = this, each = tinymce.each, s = t.settings, ln = s.languages.split(',');

		tinymce.suffix = s.suffix;

		function load(u) {
			tinymce.ScriptLoader.markDone(tinyMCE.baseURI.toAbsolute(u));
		};

		// Add core languages
		each(ln, function(c) {
			if (c)
				load('langs/' + c + '.js');
		});

		// Add themes with languages
		each(s.themes.split(','), function(n) {
			if (n) {
				load('themes/' + n + '/editor_template' + s.suffix + '.js');

				each (ln, function(c) {
					if (c)
						load('themes/' + n + '/langs/' + c + '.js');
				});
			}
		});

		// Add plugins with languages
		each(s.plugins.split(','), function(n) {
			if (n) {
				load('plugins/' + n + '/editor_plugin' + s.suffix + '.js');

				each(ln, function(c) {
					if (c)
						load('plugins/' + n + '/langs/' + c + '.js');
				});
			}
		});
	},

	end : function() {
        tinymce.dom.Event.domLoaded = true;
	},

	eval : function(co) {
		var w = window, t = this;
		window.tinyMCEPreInit = {"base": t.baseURL,
			"suffix": t.settings.suffix};
		if (!w.execScript) {
			if (/Gecko/.test(navigator.userAgent))
				eval(co, w); // Firefox 3.0
			else
				eval.call(w, co);
		} else
			w.execScript(co); // IE
	}
};
