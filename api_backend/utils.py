import plotly.express as px
import stripe
from django.conf import settings


def plot_chart(df):
    fig = px.line(
        x=df.date,
        y=df.price,
        labels={'x': '', 'y': 'Price €'},
        color_discrete_sequence=["green"],
    )
    fig.update_layout(
        title={
            'font_size': 22,
            'xanchor': 'center',
            'x': 0.5
        },
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
    )

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='#9CA3AF',
        title_font_color="#9CA3AF",
        title_font_size=18)
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='#9CA3AF',
        title_font_color="#9CA3AF",
        title_font_size=18)
    fig.update_layout(
        modebar_remove=[
            'zoom',
            'pan',
            'select',
            'lasso2d',
            'zoomIn2d',
            'zoomOut2d',
            'resetScale2d',
            'toImage'])
    fig.update_layout()
    config = {'displayModeBar': False, 'displaylogo': False}
    chart = fig.to_html(config)

    return chart


def price_from_product(coin_id):
    pass


def get_stripe_payment_link(coin_id):
    # Set your secret key. Remember to switch to your live secret key in production.
    # See your keys here: https://dashboard.stripe.com/apikeys
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

    url = stripe.PaymentLink.create(
        line_items=[{"price": "{{PRICE_ID}}", "quantity": 1}],
        after_completion={"type": "redirect",
                          "redirect": {"url": "https://example.com"}},
    )
