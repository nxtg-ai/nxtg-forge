"""Tests for text chart visualization utilities."""

from forge.utils.text_charts import (
    BarChart,
    LineChart,
    Sparkline,
    TrendDirection,
    TrendIndicator,
    create_bar_chart,
    create_line_chart,
    create_sparkline,
    render_trend,
)


class TestBarChart:
    """Tests for BarChart."""

    def test_basic_bar_chart(self):
        """Test basic bar chart creation."""
        data = {"Test A": 80.0, "Test B": 60.0, "Test C": 90.0}
        chart = BarChart(data=data, width=40)
        result = chart.render()

        assert "Test A" in result
        assert "Test B" in result
        assert "Test C" in result
        assert "80.0" in result
        assert "60.0" in result
        assert "90.0" in result

    def test_empty_data(self):
        """Test bar chart with empty data."""
        chart = BarChart(data={}, width=40)
        result = chart.render()
        assert result == "No data"

    def test_bar_chart_without_values(self):
        """Test bar chart without showing values."""
        data = {"Test": 50.0}
        chart = BarChart(data=data, width=20, show_values=False)
        result = chart.render()

        assert "Test" in result
        assert "50.0" not in result  # Values should not be shown

    def test_unicode_bars(self):
        """Test unicode bar characters."""
        data = {"Test": 50.0}
        chart = BarChart(data=data, width=10, use_unicode=True)
        result = chart.render()

        # Should contain either unicode bars or ASCII fallback
        assert len(result) > 0


class TestLineChart:
    """Tests for LineChart."""

    def test_basic_line_chart(self):
        """Test basic line chart creation."""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        chart = LineChart(data=data, height=10, width=20)
        result = chart.render()

        assert len(result) > 0
        # Should have multiple lines
        lines = result.split("\n")
        assert len(lines) >= 10

    def test_empty_data(self):
        """Test line chart with empty data."""
        chart = LineChart(data=[], height=10, width=20)
        result = chart.render()
        assert result == "No data"

    def test_line_chart_with_label(self):
        """Test line chart with label."""
        data = [1.0, 2.0, 3.0]
        chart = LineChart(data=data, height=5, width=10, label="Test Chart")
        result = chart.render()

        assert "Test Chart" in result

    def test_line_chart_without_axes(self):
        """Test line chart without axes."""
        data = [1.0, 2.0, 3.0]
        chart = LineChart(data=data, height=5, width=10, show_axes=False)
        result = chart.render()

        # Should not have box characters
        assert "┌" not in result
        assert "└" not in result


class TestSparkline:
    """Tests for Sparkline."""

    def test_basic_sparkline(self):
        """Test basic sparkline creation."""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        sparkline = Sparkline(data=data)
        result = sparkline.render()

        assert len(result) == len(data)
        assert len(result) > 0

    def test_empty_sparkline(self):
        """Test sparkline with empty data."""
        sparkline = Sparkline(data=[])
        result = sparkline.render()
        assert result in ["─", "-"]  # Unicode or ASCII fallback

    def test_ascii_sparkline(self):
        """Test ASCII fallback sparkline."""
        data = [1.0, 2.0, 3.0]
        sparkline = Sparkline(data=data, use_unicode=False)
        result = sparkline.render()

        # Should use ASCII characters
        assert all(c in "-.:=#" for c in result)

    def test_sparkline_variation(self):
        """Test sparkline with varying data."""
        # Low, medium, high values
        data = [10.0, 50.0, 90.0]
        sparkline = Sparkline(data=data, use_unicode=False)
        result = sparkline.render()

        # Should show variation (different characters)
        assert len(set(result)) > 1


class TestTrendIndicator:
    """Tests for TrendIndicator."""

    def test_trend_up(self):
        """Test upward trend indicator."""
        indicator = TrendIndicator(
            direction=TrendDirection.UP,
            value=90.0,
            previous=85.0,
            color=False,
        )
        result = indicator.render()

        assert "↑" in result
        assert "+5.0" in result

    def test_trend_down(self):
        """Test downward trend indicator."""
        indicator = TrendIndicator(
            direction=TrendDirection.DOWN,
            value=80.0,
            previous=85.0,
            color=False,
        )
        result = indicator.render()

        assert "↓" in result
        assert "-5.0" in result

    def test_trend_stable(self):
        """Test stable trend indicator."""
        indicator = TrendIndicator(
            direction=TrendDirection.STABLE,
            value=85.0,
            previous=85.0,
            color=False,
        )
        result = indicator.render()

        assert "→" in result

    def test_trend_without_previous(self):
        """Test trend without previous value."""
        indicator = TrendIndicator(
            direction=TrendDirection.UNKNOWN,
            value=85.0,
            previous=None,
            color=False,
        )
        result = indicator.render()

        assert "·" in result
        assert "+" not in result  # No delta without previous value


class TestConvenienceFunctions:
    """Tests for convenience functions."""

    def test_create_bar_chart(self):
        """Test create_bar_chart convenience function."""
        data = {"Test": 50.0}
        result = create_bar_chart(data)

        assert "Test" in result
        assert "50.0" in result

    def test_create_line_chart(self):
        """Test create_line_chart convenience function."""
        data = [1.0, 2.0, 3.0]
        result = create_line_chart(data)

        assert len(result) > 0

    def test_create_sparkline(self):
        """Test create_sparkline convenience function."""
        data = [1.0, 2.0, 3.0]
        result = create_sparkline(data)

        assert len(result) == len(data)

    def test_render_trend_improving(self):
        """Test render_trend for improving metric."""
        result = render_trend(value=90.0, previous=85.0, color=False)

        assert "↑" in result
        assert "+5.0" in result

    def test_render_trend_declining(self):
        """Test render_trend for declining metric."""
        result = render_trend(value=80.0, previous=85.0, color=False)

        assert "↓" in result
        assert "-5.0" in result

    def test_render_trend_no_previous(self):
        """Test render_trend without previous value."""
        result = render_trend(value=85.0, previous=None, color=False)

        assert "·" in result


class TestEdgeCases:
    """Tests for edge cases."""

    def test_single_data_point_line_chart(self):
        """Test line chart with single data point."""
        chart = LineChart(data=[5.0], height=5, width=10)
        result = chart.render()

        assert len(result) > 0

    def test_identical_values_bar_chart(self):
        """Test bar chart with identical values."""
        data = {"A": 50.0, "B": 50.0, "C": 50.0}
        chart = BarChart(data=data)
        result = chart.render()

        # All bars should be same length
        assert "50.0" in result

    def test_very_large_values(self):
        """Test charts with very large values."""
        data = {"A": 1000000.0, "B": 2000000.0}
        chart = BarChart(data=data)
        result = chart.render()

        assert "1000000.0" in result

    def test_negative_values_sparkline(self):
        """Test sparkline with negative values."""
        data = [-10.0, 0.0, 10.0]
        sparkline = Sparkline(data=data)
        result = sparkline.render()

        assert len(result) == 3
