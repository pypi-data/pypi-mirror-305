import os
import streamlit.components.v1 as components

_RELEASE = True       

if not _RELEASE:
    _chart_to_display = components.declare_component(
        
        "chart_to_display",

        url="http://localhost:3001",
    )
else:

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _chart_to_display = components.declare_component("chart_to_display", path=build_dir)

def chart_to_display(
        chartType="pieChart", 
        chartData=None, 
        styles=None, 
        chartLayout=None, 
        scatterPlotCustom={ "customComponent": True, "customTooltip": False }, 
        lineChartCustom=False,
        lineChartCustomDetails=None,
        customNodeSize=None,
        scatterToolTipStyle=None,
        customBottomAxis=True,
        customTopAxis=False,
        customLeftAxis=False,
        customRightAxis=False, 
        customAxisWidthWrap=70,
        customAxisTranslate={"x":0, "y":30},
        customAxisTextPosition="middle",
        customAxisTextStyle=None,
        customToolTipBar=False, 
        customToolTipBarId=None,
        customToolTipBarStyle=None,
        key=None, 
        default=None
        ):
    
    component_value = _chart_to_display(
        chartType=chartType, 
        chartData=chartData, 
        chartLayout=chartLayout, 
        styles=styles, 
        scatterPlotCustom=scatterPlotCustom, 
        lineChartCustom=lineChartCustom,
        lineChartCustomDetails=lineChartCustomDetails,
        customNodeSize=customNodeSize,
        scatterToolTipStyle=scatterToolTipStyle,
        customBottomAxis=customBottomAxis,
        customTopAxis=customTopAxis,
        customLeftAxis=customLeftAxis,
        customRightAxis=customRightAxis,
        customAxisWidthWrap=customAxisWidthWrap,
        customAxisTranslate=customAxisTranslate, 
        customAxisTextPosition=customAxisTextPosition,
        customAxisTextStyle=customAxisTextStyle,
        customToolTipBar=customToolTipBar,
        customToolTipBarId=customToolTipBarId,
        customToolTipBarStyle=customToolTipBarStyle,
        key=key, 
        default=default
        )

    return component_value
