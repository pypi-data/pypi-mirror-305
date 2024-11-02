'''
# Output Module

**Project Name**: outputs

**Author**: Pinpe ([https://pinpe.top](https://pinpe.top))

**Encoding**: UTF-8

**License**: MIT License

**Dependencies**: `conkits` (optional)、`requests` (optional)

**Version**: 1.14 (2024-11-1)

**Description:**
This is a Python library designed to extend the functionality of CLI printing. The primary development focus is on logging features similar to `logging`, but it also includes other functionalities and supports a high-fidelity style for PinkShell.

**Advantages:**
- Simple to learn with support for some customization.
- All-in-one functionality that includes log output, loading text, color classes, cursor control, and more.
- Easy configuration without the need to alter your project structure.
- Extremely lightweight, consisting of a single file, and requires only two standard libraries and one optional third-party library.
- Fully open-source with no backdoors.
- Comprehensive error handling, type checking, and docstrings.

**Getting Started:**
1. Install by entering this command in your terminal: `pip install outputs`
2. Import the library into your program: `from outputs import *`

**Update Notes:**
- Added more emoji mappings.
- Added special character mappings.
- Add a docstring for each class.
- Add a docstring for each module.
- Add text formatting.
'''

'''错误捕获'''
def traceback(var: object) -> None:
    '''
    **用途**：自动捕获代码中的异常，替代原生的traceback。\n
    **使用示例**：\n
    ```
    try:
        output.echo(1/0)
    except Exception as err:
        traceback(err)
    ```
    **参数用途**：
    - `var`：赋值后异常对象的名称。
    '''
    log.fatal(str(var))
    return None


try:
    '''导入依赖库'''
    import time, inspect
    from tkinter.messagebox import *


    '''内部对象，不推荐外部使用'''
    # 类型检查
    def _type(type: type, var: object, name: str) -> None:
        if type == bool:
            if not isinstance(var, bool):
                raise TypeError(f'此方法的{name}参数只能传递布尔值。')
        elif type == int | float:
            if not isinstance(var, int | float):
                raise TypeError(f'此方法的{name}参数只能传递整型和浮点型。')
        elif type == int:
            if not isinstance(var, int):
                raise TypeError(f'此方法的{name}参数只能传递整型。')
        elif type == list:
            if not isinstance(var, list):
                raise TypeError(f'此方法的{name}参数只能传递列表。')
        return None

    # 获取文件路径
    def _file() -> str:
        frame = inspect.currentframe()
        outer_frame = frame.f_back
        caller_frame = outer_frame.f_back
        file_name = inspect.getfile(caller_frame)
        return f"{file_name}"

    # 全局变量
    class _state:
        quit = True
        include_time = False
        file = False
        icon = False
        on_color = True
        buzz = False
        verbatim = 0
        pinkshell = False
        serial = False
        serial_sum = 1
        list_serial = False
        horizon_lenght = 50
        note_lenght = 500
        popup_window = True

    # 日志屏蔽变量
    class _screened:
        error = False
        warn = False
        fatal = False
        info = False
        debug = False


    '''全局配置'''
    def config(quit: bool = True, popup_window: bool = True, include_time: bool = False, file: bool = False, serial: bool = False, list_serial: bool = False,horizon_lenght: int = 50, note_lenght: int = 500, buzz: bool = False, icon: bool = False, verbatim: int | float = 0, pinkshell:bool = False, on_color: bool = True) -> None:
        '''
        **用途**：对输出进行全局配置，所有输出的配置都会被覆盖，除非单独配置。\n
        **使用示例**：\n
        ```
        config(
            quit = False,
            file = True,
            include_time = True,
            on_color = False
        )
        ```
        **参数用途**：
        - `quit`：打印完成后是否退出程序。
        - `popup_window`：是否弹出窗口。（需要GUI）
        - `include_time`：是否打印时间。
        - `file`：是否打印调用者的文件路径。
        - `serial`：是否显示序号。
        - `list_serial`：列表是否显示序号。
        - `horizon_lenght`：水平线长度。
        - `note_lenght`：记事本水平线长度
        - `buzz`：是否发出提示音。（在部分情况下可能不可用）
        - `icon`：是否打印图标。
        - `verbatim`：逐字显示的速度。
        - `pinkshell`：是否使用PinkShell模式，启用后其它配置将失效。
        - `on_color`：是否显示颜色。（需要终端支持ANSI才可用）
        '''
        for i in ('quit', 'file', 'include_time', 'icon', 'on_color', 'buzz', 'pinkshell', 'list_serial', 'popup_window'):
            exec(f"_type(bool, {i}, '{i}')")
        _type(int | float, verbatim, 'verbatim')
        _type(int, horizon_lenght, 'horizon_lenght')
        _type(int, note_lenght, 'note_lenght')
        for i in ('quit', 'file', 'include_time', 'icon', 'on_color', 'buzz', 'verbatim', 'pinkshell', 'serial', 'list_serial', 'horizon_lenght', 'note_lenght', 'popup_window'):
            exec(f'_state.{i} = {i}')
        return None


    '''日志屏蔽'''
    def screened(debug: bool = False, info: bool = False, warn: bool = False, error: bool = False, fatal: bool = False) -> None:
        '''
        **用途**：针对某些日志类型进行屏蔽，屏蔽的类型将不再输出。\n
        **使用示例**：\n
        ```
        screened(
            debug = True,
            info = True,
            warn = True
        )
        ```
        '''
        for i in ('debug', 'info', 'warn', 'error', 'fatal'):
            exec(f"_type(bool, {i}, '{i}')")
        for i in ('debug', 'info', 'warn', 'error', 'fatal'):
            exec(f"_screened.{i} = {i}")
        return None


    '''样式类'''
    # 预设与常用
    '''
    **用途**：给文字加上预设样式和复原样式。\n
    **包含**：`rst`、`title1`、`title2`、`em`、`link`、`exegesis`、`important`、`warn`、`tip`\n
    **注意**：为了调用方便，没有设置一个正式的类，但开发时最好看成一个整体。
    '''
    rst = '\033[m'
    title1 = '\033[1m\033[43m\033[30m'
    title2 = '\033[1m\033[4m\033[33m'
    em = '\033[1m\033[33m'
    link = '\033[4m\033[34m'
    exegesis = '\033[36m> '
    important = '\033[1m\033[31m重要警告：'
    warn = '\033[1m\033[33m警告：'
    tip = '\033[1m\033[34m提示：'

    # 前景色
    class color:
        '''
        **用途**：给文字加上前景色。\n
        **包含**：`black`、`red`、`green`、`yellow`、`blue`、`purple`、`cyan`、`white`
        '''
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        yellow = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        white = '\033[37m'

    # 背景色
    class back:
        '''
        **用途**：给文字加上背景色。\n
        **包含**：`black`、`red`、`green`、`yellow`、`blue`、`purple`、`cyan`、`white`
        '''
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        yellow = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        white = '\033[47m'

    # 样式
    class style:
        '''
        **用途**：给文字加上特殊样式。\n
        **包含**：`bold`、`underline`、`blink`、`invis`、`rev`
        '''
        bold = '\033[1m'
        underline = '\033[4m'
        blink = '\033[5m'
        invis = '\033[8m'
        rev = '\033[7m'


    '''emoji类'''
    class emoji:
        '''
        **用途**：插入emoji。\n
        **内容**：略
        '''
        nerd_face = '🤓'
        check_mark = '✅'
        fire = '🔥'
        china_flag = '🇨🇳'
        hands_clapping_heart = '🫶'
        clown_face = '🤡'
        location_pin = '📍'
        hand_with_finger_curling = '🫡'
        no_one_under_eighteen = '🔞'
        sweat_smile = '😅'
        eye = '👁'
        cat_face = '🐱'
        speaker = '🔈'
        transgender = '🏳️‍⚧️'
        alien = '👽'
        rabbit_head = '🐰'
        white_flower = '💮'
        seedling = '🌱'
        x = '❌'
        warning = '⚠️'
        rolling_on_the_floor_with_laughter = '🤣'
        tomato = '🍅'
        pizza = '🍕'
        headphones = '🎧'
        music_note = '🎵'
        iphone = '📱'
        scissors = '✂'
        compass = '🧭'
        cherries = '🍒'
        heart_eyes = '😍'
        smiley_face = '😃'
        slightly_smiling_face = '🙂'
        face_with_tongue = '😛'
        winking_face = '😉'
        star_struck = '🤩'
        thinking_face = '🤔'
        disappointed_face = '😔'
        angry_face = '😠'
        crying_face = '😢'
        face_screaming_in_fear = '😱'
        face_with_monocle = '🧐'
        hugging_face = '🤗'
        kissing_face = '😘'
        smiling_face_with_heart_eyes = '🥰'
        face_blowing_a_kiss = '😘'
        confused_face = '😕'
        dizzy_face = '😵'
        zombie = '🧟'
        ghost = '👻'
        skull = '💀'
        pile_of_poo = '💩'
        chicken = '🐔'
        dog_face = '🐶'
        monkey_face = '🐒'
        panda_face = '🐼'
        tiger_face = '🐯'
        pig_face = '🐷'
        frog_face = '🐸'
        snail = '🐌'
        butterfly = '🦋'
        elephant = '🐘'
        giraffe = '🦒'
        shark = '🦈'
        whale = '🐳'
        sun_with_face = '🌞'
        moon_with_face = '🌙'
        earth_globe = '🌍'
        comet = '☄️'
        shooting_star = '✨'
        rainbow = '🌈'
        umbrella = '🌂'
        cloud_with_rain = '🌧️'
        sun_behind_cloud = '⛅'
        snowflake = '❄️'
        leaf_fluttering_in_wind = '🍃'
        flower_blooming = '🌼'
        water_wave = '🌊'
        volcano = '🌋'
        mountain = '🏔️'
        castle = '🏰'
        house = '🏠'
        school = '🏫'
        hospital = '🏥'
        bank = '🏦'
        post_office = '🏣'
        church = '⛪'
        mosque = '🕌'
        synagogue = '🕍'
        love_hotel = '🏩'
        building_construction = '🏗️'
        statue_of_liberty = '🗽'
        eiffel_tower = '🗼'
        colosseum = '🏛️'


    '''特殊符号映射'''
    class notation:
        '''
        **用途**：插入特殊符号。\n
        **内容**：略
        '''
        infinite = '∞'
        because = '∵'
        so = '∴'
        plus_minus = '±'
        not_equal = '≠'
        less_or_equal = '≤'
        greater_or_equal = '≥'
        approximately_equal = '≈'
        integral = '∫'
        nabla = '∇'
        partial_derivative = '∂'
        infinity = '∞'
        square_root = '√'
        cube_root = '∛'
        fourth_root = '∜'
        angle = '∠'
        perpendicular = '⊥'
        parallel = '∥'
        triangle = '△'
        circle = '○'
        dot_product = '·'
        cross_product = '×'
        right_arrow = '→'
        left_arrow = '←'
        up_arrow = '↑'
        down_arrow = '↓'
        double_right_arrow = '⇒'
        double_left_arrow = '⇐'
        double_up_arrow = '⇑'
        double_down_arrow = '⇓'
        northeast_arrow = '↗'
        southeast_arrow = '↘'
        southwest_arrow = '↙'
        northwest_arrow = '↖'
        right_double_arrow = '⇌'
        left_double_arrow = '⇋'
        dollar = '$'
        euro = '€'
        pound = '£'
        yen = '¥'
        cent = '¢'
        rupee = '₹'
        won = '₩'
        celsius = '℃'
        degree_fahrenheit = '℉'
        copyright = '©'
        registered = '®'
        trademark = '™'
        paragraph = '¶'
        section = '§'
        bullet = '•'
        heart = '❤'
        spade = '♠'
        club = '♣'
        diamond = '♦'
        star = '★'
        check_mark = '✓'
        cross_mark = '✗'
        skull_crossbones = '☠'
        warning = '⚠'
        snowman = '☃'
        umbrella = '☂'
        sun = '☀'
        moon = '☾'
        earth = '♁'
        mercury = '☿'
        venus = '♀'
        mars = '♂'
        jupiter = '♃'
        saturn = '♄'
        uranus = '♅'
        neptune = '♆'
        pluto = '♇'
        black_square = '■'
        white_square = '□'
        black_circle = '●'
        white_circle = '○'
        black_triangle = '▲'
        white_triangle = '△'
        black_diamond = '◆'
        white_diamond = '◇'
        black_heart = '❤'
        white_heart = '♡'
        black_spade = '♠'
        white_spade = '♤'
        black_club = '♣'
        white_club = '♧'
        black_diamond_suit = '♦'
        white_diamond_suit = '♢'


    '''输出类'''
    class output:
        '''
        **用途**：各种输出模式，例如进度条、菜单、水平线等。\n
        **包含**：`echo()`、`bar()`、`menu()`、`li()`、`horizon()`、`note()`
        '''
        # 普通输出
        echo = print

        # 加载文字
        @staticmethod
        def load(text: str, sum: int | float) -> None:
            '''
            **用途**：打印加载文字，后面还有动态的加载动画。\n
            **使用示例**：`output.load('text', sum = 3)`\n
            **参数用途**：
            - `text`: 需要打印的字符串。
            - `sum`：加载动画转几圈后完成。
            '''
            _type(int | float, sum, 'sum')
            timeflush=0.25
            for i in range(0, int(sum/timeflush)):
                list = ["\\", "|", "/", "—"]
                index = i % 4
                print("\r"+text+' {}'.format(list[index]),end='')
                time.sleep(timeflush)
            return None

        # 进度条
        @staticmethod
        def bar(text1: str, text2: str, sum: int | float) -> None:
            '''
            **用途**：打印进度条（不定宽，如果屏幕不够宽无法正常运行）。\n
            **使用示例**：`output.bar('正在加载', '加载完成', sum = 10)`\n
            **参数用途**：
            - `text1`: 加载提示字符串。
            - `text2`: 加载完成字符串。
            - `sum`：多少时间后完成。
            '''
            _type(int | float, sum, 'sum')
            timeflush = 0.5
            for i in range(0, int(sum/timeflush)+1):
                print("\r"+text1 + "|" + "*" * i + " "*(int(sum/timeflush)+1-i)+"|" + str(i), end="")
                time.sleep(timeflush)
            print("\r"+text2)
            return None

        # 菜单
        @staticmethod
        def menu(text: list, click: list) -> None:
            '''
            **用途**：打印菜单，W和S选择，Enter确定\n
            **使用示例**：`output.menu(text = ['运行A函数', '运行B函数'], click = [funcA, funcB])`\n
            **参数用途**：
            - `text`：选项文案。
            - `click`：点击选项后运行的函数。（不需要写括号）\n
            **注意**：使用前请安装conkits库，`text`与`click`一一对应。
            '''
            _type(list, text, 'text')
            _type(list, click, 'click')
            from conkits import Choice
            option = Choice(options = text, methods = click)
            option.run()
            return None

        # 列表
        @staticmethod
        def li(text: list, list_serial: bool = None) -> None:
            '''
            **用途**：格式化打印列表\n
            **使用示例**：`output.li(['香蕉', '苹果'])`\n
            **参数用途**：
            - `text`：列表文案。
            - `list_serial`：是否显示序号\n
            '''
            list_serial = list_serial if list_serial is not None else _state.list_serial
            _type(bool, list_serial, 'order')
            serial_sum = 1 if list_serial else '-'
            for i in text:
                print(f"{serial_sum}{'.' if list_serial else ''} {i}")
                serial_sum += 1 if list_serial else ''
            return None

        # 水平线
        @staticmethod
        def horizon(element: str = '─', horizon_lenght: int = None) -> None:
            '''
            **用途**：绘制水平线\n
            **使用示例**：`output.horizon()`\n
            **参数用途**：
            - `element`：构成的字符。
            - `horizon_lenght`：水平线的长度。\n
            '''
            horizon_lenght = horizon_lenght if horizon_lenght is not None else _state.horizon_lenght
            _type(int, horizon_lenght, 'sum')
            print(f'{element}' * horizon_lenght)
            return None

        # 仿记事本样式
        @staticmethod
        def note(text: str, note_lenght: int = None) -> None:
            '''
            **用途**：模仿记事本样式来输出文字（只能支持特定格式）\n
            **使用示例**：`output.note()`\n
            **参数用途**：
            - `element`：要打印的文字。
            - `horizon_lenght`：记事本水平线的长度。\n
            '''
            note_lenght = note_lenght if note_lenght is not None else _state.note_lenght
            _type(int, note_lenght, 'sum')
            print(f"{style.underline}{text}{' ' * note_lenght}")
            return None


    '''日志类'''
    class log:
        '''
        **用途**：输出各种日志。\n
        **包含**：`error()`、`warn()`、`fatal()`、`info()`、`debug()`
        '''
        # 错误输出
        @staticmethod
        def error(text: str, include_time: bool = None, file: bool = None, serial: bool = None,buzz: bool = None, icon: bool = None, verbatim: int | float = None, pinkshell: bool = None, on_color: bool = None) -> None:
            '''
            **用途**：打印错误消息。\n
            **使用示例**：`log.error('text')`\n
            **参数用途**：
            - `text`: 需要打印的字符串。
            - `include_time`：是否打印时间。
            - `file`：是否打印调用者的文件路径。
            - `serial`：是否显示序号。
            - `buzz`：是否发出提示音。（在部分情况下可能不可用）
            - `icon`：是否打印图标。
            - `verbatim`：逐字显示的速度。
            - `pinkshell`：是否使用PinkShell模式，启用后其它配置将失效。
            - `on_color`：是否显示颜色。（需要终端支持ANSI才可用）
            '''
            include_time = include_time if include_time is not None else _state.include_time
            icon = icon if icon is not None else _state.icon
            on_color = on_color if on_color is not None else _state.on_color
            file = file if file is not None else _state.file
            buzz = buzz if buzz is not None else _state.buzz
            verbatim = verbatim if verbatim is not None else _state.verbatim
            pinkshell = pinkshell if pinkshell is not None else _state.pinkshell
            serial = serial if serial is not None else _state.serial
            for i in ('file', 'include_time', 'icon', 'on_color', 'buzz', 'pinkshell', 'serial'):
                exec(f"_type(bool, {i}, '{i}')")
            _type(int | float, verbatim, 'verbatim')
            if pinkshell is False:
                time_text = f"[{time.asctime()}]" if include_time else ""
                add_color = color.red if on_color else ""
                color_rst = style.rst if on_color else ""
                add_icon = '[X]' if icon else ''
                file_text = f'[{_file()}]' if file else ''
                buzz_text = '\a' if buzz else ''
                serial_text = f'[{_state.serial_sum}]' if serial else ''
                char = f"{add_color}{serial_text}{add_icon}{time_text}{file_text}[Error] {text}{color_rst}{buzz_text}"
                for i in list(char):
                    print(i, end = '', flush = True) if not _screened.error else None
                    time.sleep(verbatim)
                print() if not _screened.error else None
                _state.serial_sum += 1
            elif pinkshell is True:
                print(f'\n{color.red}{back.white}X{style.rst}{color.white}{back.red}错误{style.rst}\n{color.red}{text}{style.rst}\n') if not _screened.error else None
                _state.serial_sum += 1
            return None

        # 警告输出
        @staticmethod
        def warn(text: str, include_time: bool = None, file: bool = None, serial: bool = None, buzz: bool = None, icon: bool = None, verbatim: int | float = None, pinkshell: bool = None, on_color: bool = None) -> None:
            '''
            **用途**：打印警告消息。\n
            **使用示例**：`log.warn('text')`\n
            **参数用途**：
            - `text`: 需要打印的字符串。
            - `include_time`：是否打印时间。
            - `file`：是否打印调用者的文件路径。
            - `serial`：是否显示序号。
            - `buzz`：是否发出提示音。（在部分情况下可能不可用）
            - `icon`：是否打印图标。
            - `verbatim`：逐字显示的速度。
            - `pinkshell`：是否使用PinkShell模式，启用后其它配置将失效。
            - `on_color`：是否显示颜色。（需要终端支持ANSI才可用）
            '''
            include_time = include_time if include_time is not None else _state.include_time
            icon = icon if icon is not None else _state.icon
            on_color = on_color if on_color is not None else _state.on_color
            file = file if file is not None else _state.file
            buzz = buzz if buzz is not None else _state.buzz
            verbatim = verbatim if verbatim is not None else _state.verbatim
            pinkshell = pinkshell if pinkshell is not None else _state.pinkshell
            serial = serial if serial is not None else _state.serial
            for i in ('file', 'include_time', 'icon', 'on_color', 'buzz', 'pinkshell', 'serial'):
                exec(f"_type(bool, {i}, '{i}')")
            _type(int | float, verbatim, 'verbatim')
            if pinkshell is False:
                time_text = f"[{time.asctime()}]" if include_time else ""
                add_color = color.yellow if on_color else ""
                color_rst = style.rst if on_color else ""
                add_icon = '[!]' if icon else ''
                file_text = f'[{_file()}]' if file else ''
                buzz_text = '\a' if buzz else ''
                serial_text = f'[{_state.serial_sum}]' if serial else ''
                char = f'{add_color}{serial_text}{add_icon}{time_text}{file_text}[Warn] {text}{color_rst}{buzz_text}'
                for i in list(char):
                    print(i, end = '', flush = True) if not _screened.warn else None
                    time.sleep(verbatim)
                print() if not _screened.fatal else None
                _state.serial_sum += 1
            elif pinkshell is True:
                print(f'\n{color.yellow}{back.white}!{style.rst}{color.white}{back.yellow}警告{style.rst}\n{color.yellow}{text}{style.rst}\n') if not _screened.warn else None
                _state.serial_sum += 1
            return None

        # 致命错误输出
        @staticmethod
        def fatal(text: str, quit: bool = None, popup_window: bool = None, include_time: bool = None, file: bool = None, serial: bool = None, buzz: bool = None, icon: bool = None, verbatim: int | float = None, pinkshell: bool = None, on_color: bool = None) -> None:
            '''
            **用途**：打印致命错误消息，最高优先级。\n
            **使用示例**：`log.fatal('text')`\n
            **参数用途**：
            - `text`: 需要打印的字符串。
            - `quit`：打印完成后是否退出程序。
            - `popup_window`：是否弹出窗口。（需要GUI）
            - `include_time`：是否打印时间。
            - `file`：是否打印调用者的文件路径。
            - `serial`：是否显示序号。
            - `buzz`：是否发出提示音。（在部分情况下可能不可用）
            - `icon`：是否打印图标。
            - `verbatim`：逐字显示的速度。
            - `pinkshell`：是否使用PinkShell模式，启用后除quit其它配置将失效。
            - `on_color`：是否显示颜色。（需要终端支持ANSI才可用）
            '''
            quit = quit if quit is not None else _state.quit
            include_time = include_time if include_time is not None else _state.include_time
            icon = icon if icon is not None else _state.icon
            on_color = on_color if on_color is not None else _state.on_color
            file = file if file is not None else _state.file
            buzz = buzz if buzz is not None else _state.buzz
            verbatim = verbatim if verbatim is not None else _state.verbatim
            pinkshell = pinkshell if pinkshell is not None else _state.pinkshell
            serial = serial if serial is not None else _state.serial
            popup_window = popup_window if popup_window is not None else _state.popup_window
            for i in ('file', 'include_time', 'icon', 'on_color', 'buzz', 'pinkshell', 'quit', 'serial', 'popup_window'):
                exec(f"_type(bool, {i}, '{i}')")
            _type(int | float, verbatim, 'verbatim')
            if pinkshell is False:
                time_text = f"[{time.asctime()}]" if include_time else ""
                add_color = color.purple if on_color else ""
                color_rst = style.rst if on_color else ""
                add_icon = '[-]' if icon else ''
                file_text = f'[{_file()}]' if file else ''
                buzz_text = '\a' if buzz else ''
                serial_text = f'[{_state.serial_sum}]' if serial else ''
                char = f"{add_color}{serial_text}{add_icon}{time_text}{file_text}[Fatal] {text}{color_rst}{buzz_text}"
                for i in list(char):
                    print(i, end = '', flush = True) if not _screened.fatal else None
                    time.sleep(verbatim)
                print() if not _screened.fatal else None
                iris.error(text, title = '致命错误') if popup_window and not _screened.fatal else None
                exit(1) if not _screened.fatal and quit else None
                _state.serial_sum += 1
            elif pinkshell is True:
                print(f'\n{color.purple}{back.white}-{style.rst}{color.white}{back.purple}致命错误{style.rst}\n{color.purple}{text}{style.rst}\n') if not _screened.fatal else None
                iris.error(text, title = '致命错误') if popup_window and not _screened.fatal else None
                exit(1) if not _screened.fatal and quit else None
                _state.serial_sum += 1
            return None

        # 信息输出
        @staticmethod
        def info(text: str, include_time: bool = None, file: bool = None, serial: bool = None, icon: bool = None, verbatim: int | float = None, pinkshell: bool = None, on_color: bool = None) -> None:
            '''
            **用途**：打印信息消息。\n
            **使用示例**：`log.info('text')`\n
            **参数用途**：
            - `text`: 需要打印的字符串。
            - `include_time`：是否打印时间。
            - `file`：是否打印调用者的文件路径。
            - `serial`：是否显示序号。
            - `icon`：是否打印图标。
            - `verbatim`：逐字显示的速度。
            - `pinkshell`：是否使用PinkShell模式，启用后其它配置将失效。
            - `on_color`：是否显示颜色。（需要终端支持ANSI才可用）
            '''
            include_time = include_time if include_time is not None else _state.include_time
            icon = icon if icon is not None else _state.icon
            on_color = on_color if on_color is not None else _state.on_color
            file = file if file is not None else _state.file
            verbatim = verbatim if verbatim is not None else _state.verbatim
            pinkshell = pinkshell if pinkshell is not None else _state.pinkshell
            serial = serial if serial is not None else _state.serial
            for i in ('file', 'include_time', 'icon', 'on_color', 'pinkshell', 'serial'):
                exec(f"_type(bool, {i}, '{i}')")
            _type(int | float, verbatim, 'verbatim')
            if pinkshell is False:
                time_text = f"[{time.asctime()}]" if include_time else ""
                add_color = color.blue if on_color else ""
                color_rst = style.rst if on_color else ""
                add_icon = '[i]' if icon else ''
                file_text = f'[{_file()}]' if file else ''
                serial_text = f'[{_state.serial_sum}]' if serial else ''
                char = f"{add_color}{serial_text}{add_icon}{time_text}{file_text}[Info] {text}{color_rst}"
                for i in list(char):
                    print(i, end = '', flush = True) if not _screened.info else None
                    time.sleep(verbatim)
                print() if not _screened.info else None
                _state.serial_sum += 1
            elif pinkshell is True:
                print(f'\n{color.blue}{back.white}i{style.rst}{color.white}{back.blue}提示{style.rst}\n{color.blue}{text}{style.rst}\n') if not _screened.info else None
                _state.serial_sum += 1
            return None

        # 调试输出
        @staticmethod
        def debug(text: str, verbatim: int | float = None) -> None:
            '''
            **用途**：打印调试消息，最低优先级。\n
            **使用示例**：`log.debug('text')`\n
            **参数用途**：
            - `text`: 需要打印的字符串。
            - `verbatim`：是否逐字显示。
            '''
            verbatim = verbatim if verbatim is not None else _state.verbatim
            _type(int | float, verbatim, 'verbatim')
            char = '[Debug] '+text
            for i in list(char):
                print(i, end = '', flush = True) if not _screened.debug else None
                time.sleep(verbatim)
            print() if not _screened.debug else None
            return None


    '''键盘输入'''
    def keyboard(text: str = '', include_time: bool = None, buzz: bool = None) -> object:
        '''
            **用途**：获取键盘输入，可以存储在变量中，类似`input()`。\n
            **使用示例**：`keyboard()`\n
            **参数用途**：
            - `text`: 给用户的提示。
            - `include_time`：是否打印时间。
            - `buzz`：是否发出提示音。（在部分情况下可能不可用）
        '''
        include_time = include_time if include_time is not None else _state.include_time
        buzz = buzz if buzz is not None else _state.buzz
        _type(bool, include_time, 'include_time')
        _type(bool, buzz, 'buzz')
        time_text = f"[{time.asctime()}]" if include_time else ""
        buzz_text = '\a' if buzz else ''
        print(f'{time_text}{buzz_text}{text} -> ',end='')
        return input()


    '''清屏类'''
    class clean:
        '''
        **用途**：清空文本。\n
        **包含**：`screen()`、`line()`
        '''
        @staticmethod
        def screen() -> None:
            '''
            **用途**：清空屏幕\n
            **使用示例**：`clean.screen()`\n
            '''
            print('\033[2J')
            print('\033[H', end='')
            return None

        @staticmethod
        def line() -> None:
            '''
            **用途**：清空光标所在的行（不会复位光标）\n
            **使用示例**：`clean.line()`\n
            '''
            print('\033[2K', end='')
            return None


    '''光标控制类'''
    class cursor:
        '''
        **用途**：控制光标的可见性。\n
        **包含**：`show()`、`hide()`
        '''
        @staticmethod
        def show() -> None:
            '''
            **用途**：显示光标\n
            **使用示例**：`cursor.show()`\n
            '''
            print('\033[?25h',end='')
            return None

        @staticmethod
        def hide() -> None:
            '''
            **用途**：隐藏光标\n
            **使用示例**：`cursor.hide()`\n
            '''
            print('\033[?25l',end='')
            return None


    '''窗口类'''
    class iris:
        '''
        **用途**：弹出各种提示或询问窗口。\n
        **包含**：`error()`、`worn()`、`info()`、`y_n()`、`ok_cancel()`、`y_n_cancel()`
        '''
        # 错误窗口
        @staticmethod
        def error(text: str, title: str = '错误') -> None:
            '''
            **用途**：弹出错误窗口。\n
            **使用示例**：`iris.error('出现了一个错误！')`\n
            **参数用途**：
            - `text`: 显示内容。
            - `title`：窗口标题。
            '''
            showerror(title, text)
            return None

        # 警告窗口
        @staticmethod
        def worn(text: str, title: str = '警告') -> None:
            '''
            **用途**：弹出警告窗口。\n
            **使用示例**：`iris.worn('这是一个警告！')`\n
            **参数用途**：
            - `text`: 显示内容。
            - `title`：窗口标题。
            '''
            showwarning(title, text)
            return None

        # 提示窗口
        @staticmethod
        def info(text: str, title: str = '提示') -> None:
            '''
            **用途**：弹出提示窗口。\n
            **使用示例**：`iris.info('Hello')`\n
            **参数用途**：
            - `text`: 显示内容。
            - `title`：窗口标题。
            '''
            showinfo(title, text)
            return None

        # 是/否窗口
        @staticmethod
        def y_n(text: str, title: str = '请选择') -> object:
            '''
            **用途**：弹出“是/否”选择窗口，选择结果可以存储在变量中。\n
            **使用示例**：`iris.yes_no('你玩原神吗？')`\n
            **参数用途**：
            - `text`: 显示内容。
            - `title`：窗口标题。
            '''
            return askyesno(title, text)

        # 确定/取消窗口
        @staticmethod
        def ok_cancel(text: str, title: str = '请选择') -> object:
            '''
            **用途**：弹出“确定/取消”选择窗口，选择结果可以存储在变量中。\n
            **使用示例**：`iris.ok_cancel('确定关闭程序？')`\n
            **参数用途**：
            - `text`: 显示内容。
            - `title`：窗口标题。
            '''
            return askokcancel(title, text)

        # 是/否/取消窗口
        @staticmethod
        def y_n_cancel(text: str, title: str = '请选择') -> object:
            '''
            **用途**：弹出“是/否/取消”选择窗口，选择结果可以存储在变量中。\n
            **使用示例**：`iris.y_n_cancel('还有文件未保存，是否现在保存？')`\n
            **参数用途**：
            - `text`: 显示内容。
            - `title`：窗口标题。
            '''
            return askyesnocancel(title, text)


    '''跳转页面'''
    def goto_page(destination: str) -> None:
        '''
        **用途**：跳转到目标页面。\n
        **使用示例**：`goto_page('func')`\n
        **参数用途**：
        - `destination`：要跳转到的页面函数名称。（字符串）
        '''
        clean.screen()
        exec(f'{destination}()')
        return None


    '''一言'''
    def hitokoto() -> str:
        '''
        **用途**：请求一句一言。\n
        **使用示例**：`hitokoto()`\n
        **注意**：使用前请安装requests库。
        '''
        import requests
        return requests.get('https://v1.hitokoto.cn/?encode=text').text


    '''关于库'''
    def about() -> None:
        '''
        **用途**：打印库的相关信息。\n
        **使用示例**：`about()`\n
        '''
        print(f'''{color.blue}
 ██████╗ ██╗   ██╗████████╗██████╗ ██╗   ██╗████████╗
██╔═══██╗██║   ██║╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝
██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║
██║   ██║██║   ██║   ██║   ██╔═══╝ ██║   ██║   ██║
╚██████╔╝╚██████╔╝   ██║   ██║     ╚██████╔╝   ██║
 ╚═════╝  ╚═════╝    ╚═╝   ╚═╝      ╚═════╝    ╚═╝

{color.green}{style.bold}作者：{style.rst}Pinpe
{color.green}{style.bold}版本：{style.rst}1.14（2024年11月1日更新）
{color.green}{style.bold}依赖库：{style.rst}conkits（可选）

{back.red}   {back.green}   {back.blue}   {back.yellow}   {back.purple}   {back.cyan}   {back.black}   {back.white}   {style.rst}
''')
        return None
except Exception as err:
    traceback(err)