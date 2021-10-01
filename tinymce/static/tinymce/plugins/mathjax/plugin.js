tinymce.PluginManager.add('mathjax', function (editor, url) {
    // plugin configuration options
    let symbols = [
        {name: '$$', regex: '^\\$\\$([^$]+)\\$\\$$'},
        {name: '$', regex: '^\\$([^$]+)\\$$'}
    ]
    let mathjaxClassName = 'math-tex';
    let mathjaxTempClassName = 'math-tex-original';
    let mathjaxScriptSrc = url + '/mathjax.min.js'
    let mathjaxConfig = 'MathJax = {\n' +
        'tex: {\n' +
        'inlineMath: [["$", "$"], ["\\(", "\\)"]]\n' +
        '}\n' +
        '};';

    let refreshMathJax = function (editor) {
        if (editor.getDoc().defaultView.MathJax && editor.getDoc().defaultView.MathJax.startup) {
            editor.getDoc().defaultView.MathJax.startup.getComponents();
            editor.getDoc().defaultView.MathJax.typeset();
        }
    }

    let checkElement = function (element) {
        if (element.childNodes.length != 2) {
            element.setAttribute('contenteditable', false);
            element.style.cursor = 'pointer';
            let latex = element.getAttribute('data-latex') || element.innerHTML;
            element.setAttribute('data-latex', latex);
            element.innerHTML = '';

            let math = editor.dom.create('span');
            math.innerHTML = latex;
            math.classList.add(mathjaxTempClassName);
            element.appendChild(math);

            let dummy = editor.dom.create('span');
            dummy.classList.add('dummy');
            dummy.innerHTML = 'dummy';
            dummy.setAttribute('hidden', 'hidden');
            element.appendChild(dummy);
        }
    };

    let getMathText = function (latex, symbol) {
        return symbol + ' ' + latex + ' ' + symbol;
    };

    // load mathjax and its config on editor init
    editor.on('init', function () {
        let mathjaxConfigScript = editor.dom.create('script', {
            id: editor.dom.uniqueId(),
            type: 'text/javascript',
            async: false
        });
        if (window.opera) {
            mathjaxConfigScript.innerHTML = mathjaxConfig
        } else {
            mathjaxConfigScript.text = mathjaxConfig
        }
        editor.getDoc().getElementsByTagName('head')[0].appendChild(mathjaxConfigScript);

        let mathjaxScript = editor.dom.create('script', {
            id: editor.dom.uniqueId(),
            type: 'text/javascript',
            src: mathjaxScriptSrc,
            async: false
        });
        editor.getDoc().getElementsByTagName('head')[0].appendChild(mathjaxScript);
    });

    // remove extra tags on get content
    editor.on('GetContent', function (e) {
        let div = editor.dom.create('div');
        div.innerHTML = e.content;
        let elements = div.querySelectorAll('.' + mathjaxClassName);
        for (let i = 0; i < elements.length; i++) {
            let children = elements[i].querySelectorAll('span');
            for (let j = 0; j < children.length; j++) {
                children[j].remove();
            }
            let latex = elements[i].getAttribute('data-latex');
            elements[i].removeAttribute('contenteditable');
            elements[i].removeAttribute('style');
            elements[i].removeAttribute('data-latex');
            elements[i].innerHTML = latex;
        }
        e.content = div.innerHTML;
    });

    // add dummy tag on set content
    editor.on('BeforeSetContent', function (e) {
        let div = editor.dom.create('div');
        div.innerHTML = e.content;
        let elements = div.querySelectorAll('.' + mathjaxClassName);
        for (let i = 0; i < elements.length; i++) {
            checkElement(elements[i]);
        }
        e.content = div.innerHTML;
    });

    // refresh mathjax on set content
    editor.on('SetContent', function (e) {
        refreshMathJax(editor);
    });

    // refresh mathjax on any content change
    editor.on('Change', function (data) {
        elements = editor.dom.getRoot().querySelectorAll('.' + mathjaxClassName);
        if (elements.length) {
            for (let i = 0; i < elements.length; i++) {
                checkElement(elements[i]);
            }
            refreshMathJax(editor);
        }
    });

    // add button to tinymce
    editor.ui.registry.addToggleButton('mathjax', {
        text: 'Σ',
        tooltip: 'Mathjax',
        onAction: function () {
            let selected = editor.selection.getNode();
            let target = undefined;
            if (selected.classList.contains(mathjaxClassName)) {
                target = selected;
            }
            openMathjaxEditor(target);
        },
        onSetup: function (buttonApi) {
            return editor.selection.selectorChangedWithUnbind('.' + mathjaxClassName, buttonApi.setActive).unbind;
        }
    });

    // handle click on existing
    editor.on("click", function (e) {
        let closest = e.target.closest('.' + mathjaxClassName);
        if (closest) {
            openMathjaxEditor(closest);
        }
    });

    // open window with editor
    let openMathjaxEditor = function (target) {
        // parse initial values
        let mathjaxId = editor.id + '_' + editor.dom.uniqueId();
        let latex = undefined;
        let symbol = undefined;
        let sortedSymbols = symbols.map(s => ({text: s.name, value: s.name}));
        if (target) {
            latexAttribute = target.getAttribute('data-latex');
            for (let i = 0; i < symbols.length; i++) {
                let match = latexAttribute.match(symbols[i].regex);
                if (match && match[1]) {
                    latex = match[1].trim();
                    symbol = symbols[i].name;
                    break;
                }
            }
        }
        // if we have an initial symbol, sort our array to put it on top
        if (symbol) {
            sortedSymbols = sortedSymbols.sort((a, b) => {
                if (a.value == symbol) {
                    return 1;
                }
                if (b.value == symbol) {
                    return -1
                }
                return 0;
            })
        }

        // show new window
        editor.windowManager.open({
            title: 'Mathjax',
            width: 600,
            height: 300,
            body: {
                type: 'panel',
                items: [{
                    type: 'selectbox',
                    name: 'symbol',
                    label: 'Symbol',
                    items: sortedSymbols
                }, {
                    type: 'textarea',
                    name: 'input',
                    label: 'LaTex'
                }, {
                    type: 'htmlpanel',
                    html: '<div style="text-align:right"><a href="https://wikibooks.org/wiki/LaTeX/Mathematics" target="_blank" style="font-size:small">LaTex</a></div>'
                }, {
                    type: 'htmlpanel',
                    html: '<iframe id="' + mathjaxId + '" style="width: 100%; min-height: 50px;"></iframe>'
                }]
            },
            buttons: [{type: 'submit', text: 'OK'}],
            onSubmit: function onsubmit(api) {
                latex = api.getData().input.trim();
                symbol = api.getData().symbol.trim();
                let formattedLatex = getMathText(latex, symbol);
                if (target) {
                    target.innerHTML = '';
                    target.setAttribute('data-latex', formattedLatex);
                    checkElement(target);
                } else {
                    let newElement = editor.getDoc().createElement('span');
                    newElement.innerHTML = formattedLatex;
                    newElement.classList.add(mathjaxClassName);
                    checkElement(newElement);
                    editor.insertContent(newElement.outerHTML);
                }
                api.close();
            },
            onChange: function (api) {
                latex = api.getData().input.trim();
                symbol = api.getData().symbol.trim();
                refreshDialogMathjax(latex, symbol);
            },
            initialData: {input: latex, symbol: symbol}
        });

        // add scripts to iframe
        let iframe = document.getElementById(mathjaxId);
        let iframeWindow = iframe.contentWindow || iframe.contentDocument.document || iframe.contentDocument;
        let iframeDocument = iframeWindow.document;
        let iframeHead = iframeDocument.getElementsByTagName('head')[0];
        let iframeBody = iframeDocument.getElementsByTagName('body')[0];

        // refresh latex in mathjax iframe
        let refreshDialogMathjax = function (latex, symbol) {
            let MathJax = iframeWindow.MathJax;
            let div = iframeBody.querySelector('div');
            if (!div) {
                div = iframeDocument.createElement('div');
                div.classList.add(mathjaxTempClassName);
                iframeBody.appendChild(div);
            }
            div.innerHTML = getMathText(latex, symbol);
            if (MathJax && MathJax.startup) {
                MathJax.startup.getComponents();
                MathJax.typeset();
            }
        };
        refreshDialogMathjax(latex, symbol);

        // add config script to dialog iframe
        let mathjaxConfigScript = iframeWindow.document.createElement('script');
        mathjaxConfigScript.type = 'text/javascript';
        mathjaxConfigScript.async = false;
        mathjaxConfigScript.charset = 'utf-8';
        if (window.opera) {
            mathjaxConfigScript.innerHTML = mathjaxConfig
        } else {
            mathjaxConfigScript.text = mathjaxConfig
        }
        iframeHead.appendChild(mathjaxConfigScript);

        // add mathjax script to dialog iframe
        let mathjaxScript = iframeWindow.document.createElement('script');
        mathjaxScript.src = mathjaxScriptSrc;
        mathjaxScript.type = 'text/javascript';
        mathjaxScript.async = false;
        mathjaxScript.charset = 'utf-8';
        iframeHead.appendChild(mathjaxScript);

    };
});
