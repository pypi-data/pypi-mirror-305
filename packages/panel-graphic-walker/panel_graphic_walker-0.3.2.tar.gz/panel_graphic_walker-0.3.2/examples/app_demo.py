from io import StringIO

import pandas as pd
import panel as pn

from panel_gwalker import GraphicWalker

pn.extension("filedropper", sizing_mode="stretch_width")

PANEL_GW_URL = "https://github.com/panel-extensions/panel-graphic-walker"
GW_LOGO = "https://kanaries.net/_next/static/media/kanaries-logo.0a9eb041.png"
GW_API = "https://github.com/Kanaries/graphic-walker"
GW_GUIDE_URL = "https://docs.kanaries.net/graphic-walker/data-viz/create-data-viz"

def _label(value):
    return pn.pane.Markdown(value, margin=(-20, 5))

def _section_header(value):
    return pn.pane.Markdown(value, margin=(-5, 5))

@pn.cache
def get_data():
    return pd.read_parquet(
        "https://datasets.holoviz.org/windturbines/v1/windturbines.parq"
    )


def get_example_download():
    df = pd.DataFrame(
        {"country": ["Denmark", "Germany"], "population": [5_000_000, 80_000_000]}
    )
    sio = StringIO()
    df.to_csv(sio, index=False)
    sio.seek(0)
    return sio

button_style = dict(button_type="primary", button_style="outline")

walker = GraphicWalker(get_data(), sizing_mode="stretch_both", server_computation=True)
core_settings = pn.Column(
    walker.param.server_computation,
    walker.param.config, name="Core"

)
style_settings = pn.Column(
    _label("Appearance"),
    pn.widgets.RadioButtonGroup.from_param(walker.param.appearance, **button_style),
    _label("Theme"),
    pn.widgets.RadioButtonGroup.from_param(walker.param.theme, **button_style),
    name="Style"
)
file_upload = pn.widgets.FileDropper(
    accepted_filetypes=["text/csv"],
    multiple=False,
    max_file_size="5MB",
    styles={"border": "1px dashed black", "border-radius": "4px"},
    height=85,
)
file_download = pn.widgets.FileDownload(
    callback=get_example_download, filename="example.csv"
)

exported = pn.pane.JSON(depth=2)

mode = pn.widgets.RadioButtonGroup(
    options={'SVG': 'svg', 'Vega Spec': 'spec'}, value='spec', **button_style
)
scope = pn.widgets.RadioButtonGroup(
    options={'Current': 'current', 'All': 'all'}, value='current', **button_style
)

async def export(_):
    exported.object = await walker.export(mode=mode.value, scope=scope.value)

export_section = pn.Column(
    _section_header("## Export"),
    _label("Mode"),
    mode,
    _label("Scope"),
    scope,
    pn.widgets.Button(icon="download", on_click=export, description="Click to export"),
    exported, name="Export"
)
docs_section = f"## Docs\n\n- [panel-graphic-walker]({PANEL_GW_URL})\n- [Graphic Walker Usage Guide]({GW_GUIDE_URL})\n- [Graphic Walker API]({GW_API})"


@pn.depends(file_upload, watch=True)
def _update_walker(value):
    if value:
        text = next(iter(value.values()))
        df = pd.read_csv(StringIO(text))
        if not df.empty:
            walker.object = df


pn.template.FastListTemplate(
    logo=GW_LOGO,
    title="Panel Graphic Walker",
    sidebar=[
        file_upload,
        file_download,
        pn.Accordion(
            core_settings,
            style_settings,
            export_section,
            width=320,
            active=[0]
        ),
        docs_section,
    ],
    main=[walker],
    main_layout=None,
).servable()
