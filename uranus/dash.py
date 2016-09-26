from IPython.display import display, HTML, Javascript

def toggle():

    hider_html = '''
                <script>
                code_show=true; 
                function code_toggle() {
                if (code_show){
                    $('div.input').hide();
                    $('#notebook-container.container').css('background-color', 'transparent')
                    $('body').css('background-color', '#f5f5f5')
                    $('#notebook-container.container').css('box-shadow','none')
                    $('.output_prompt').css('visibility', 'hidden')
                    $('.input_prompt').css('min-width', '28ex')
                    $('.cell.code_cell.rendered.unselected').css('padding',0)
                    $('.cell.code_cell.rendered.unselected').css('border',0)
                    $('div.output_javascript').parent('div.output_area').css("display","none")
                    $('.cell.border-box-sizing.code_cell.rendered').css("padding",0)
                    $('.cell.border-box-sizing.code_cell.rendered').css("border",0)
                } else {
                    $('div.input').show();
                    $('#notebook-container.container').css('background-color', '#ffffff')
                    $('body').css('background-color', '#EEE')
                    $('#notebook-container.container').css('box-shadow','0px 0px 12px 1px rgba(87, 87, 87, 0.2)')
                    $('.output_prompt').css('visibility', 'visible')
                    $('.input_prompt').css('min-width', '14ex')
                    $('.cell.code_cell.rendered.unselected').css('padding',5)
                    $('.cell.code_cell.rendered.unselected').css('border',1.111)
                    $('div.output_javascript').parent('div.output_area').css("display","inline")
                    $('.cell.border-box-sizing.code_cell.rendered').css("padding",5)
                    $('.cell.border-box-sizing.code_cell.rendered').css("border",1)
                }
                    code_show = !code_show
                } 

                $( document ).ready(code_toggle);

                </script>
                <a href="javascript:code_toggle()">Code View</a></br>
                <a href="https://github.com/jstoxrocky/uranus" class="fa fa-github"> Edit on GitHub</a>
                '''

    display(HTML(hider_html))
         
def set_favicon(favicon):
    f = """$("link[rel='shortcut icon']").attr("href", "{favicon}");""".format(favicon=favicon)
    display(Javascript(f))
