import plotly.express as px

# Create color map
colors = dict(zip(star_wars_sets.set_num, star_wars_sets.rgb.apply(lambda x: "#" + x)))

# Create a strip plot of the data
fig = px.strip(
    star_wars_sets,
    x="year",
    y="num_parts",
    color="set_num",
    color_discrete_map=colors,
    custom_data=["set_name", "year", "num_parts", "color_name"],
).update_traces(dict(marker_line_width=0.5, marker_line_color="black"))

# Customize data to show
fig.update_traces(
    hovertemplate="<br>".join(
        [
            "<b>%{customdata[0]}</b>",
            "<b>Year:</b> %{customdata[1]}",
            "<b>Number of parts:</b> %{customdata[2]}",
            "<b>Most common color in set:</b> %{customdata[3]}<extra></extra>",
        ]
    ),
)

# Update the layout and show the figure
fig.update_layout(
    title="Star Wars Lego Sets<br><sup>Year of Release, Number of Parts, and Most Common Color</sup>",
    title_x=0.5,
    xaxis_title="Year of Release",
    yaxis_title="Number of Parts",
    template="plotly_white",
    coloraxis_colorbar_title_text="Total Inventory",
    showlegend=False
)

fig.show()
